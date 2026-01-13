import os
import numpy as np
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.preprocessing import image
import tensorflow as tf
import gc

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Global variables for model
model = None
IMAGE_SIZE = (350, 350)
CLASS_LABELS = ['adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib', 
                'large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa',
                'normal',
                'squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa']

# Human-readable labels
CLASS_NAMES = {
    'adenocarcinoma_left.lower.lobe_T2_N0_M0_Ib': 'Adenocarcinoma',
    'large.cell.carcinoma_left.hilum_T2_N2_M0_IIIa': 'Large Cell Carcinoma',
    'normal': 'Normal',
    'squamous.cell.carcinoma_left.hilum_T1_N2_M0_IIIa': 'Squamous Cell Carcinoma'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Global variable for error tracking
load_error = "Model initialization not attempted"

def load_model_weights():
    """Load the trained model weights"""
    global model, load_error
    try:
        # Debug info
        import os
        cwd = os.getcwd()
        files = []
        for root, dirs, filenames in os.walk('.'):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        
        # Try to load the saved model file from multiple possible locations
        possible_paths = [
            'models/best_model.hdf5',
            'best_model.hdf5',
            'data/Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main (1)/Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main/best_model.hdf5',
            'Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main (1)/Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main/best_model.hdf5',
            'Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main/Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main/best_model.hdf5'
        ]
        
        model_path = None
        for path in possible_paths:
            if os.path.exists(path):
                model_path = path
                break
        
        if model_path:
            # Reconstruct the model architecture
            pretrained_model = tf.keras.applications.Xception(
                weights='imagenet', 
                include_top=False, 
                input_shape=[*IMAGE_SIZE, 3]
            )
            pretrained_model.trainable = False
            
            model = Sequential()
            model.add(pretrained_model)
            model.add(GlobalAveragePooling2D())
            model.add(Dense(4, activation='softmax'))
            
            # Load weights
            model.load_weights(model_path)
            model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
            print("Model loaded successfully!")
            return True
        else:
            load_error = f"File not found. CWD: {cwd}. Files found: {files[:20]}..."
            print(f"Model file not found. Checked paths: {possible_paths}")
            return False
    except Exception as e:
        load_error = f"Exception loading model: {str(e)}"
        print(f"Error loading model: {str(e)}")
        return False

# ... inside predict ...
    if model is None:
        return jsonify({'error': f'Model load failed: {load_error}'}), 500
    
    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Preprocess image
        img_array = preprocess_image(filepath)
        if img_array is None:
            return jsonify({'error': 'Error processing image'}), 500
        
        # Make prediction
        predictions = model.predict(img_array, verbose=0)
        predicted_class_idx = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class_idx] * 100)
        
        predicted_class = CLASS_LABELS[predicted_class_idx]
        predicted_name = CLASS_NAMES.get(predicted_class, predicted_class)
        
        # Get all class probabilities
        all_predictions = {}
        for i, label in enumerate(CLASS_LABELS):
            class_name = CLASS_NAMES.get(label, label)
            all_predictions[class_name] = float(predictions[0][i] * 100)
        
        # Clean up uploaded file
        os.remove(filepath)
        
        return jsonify({
            'success': True,
            'prediction': predicted_name,
            'confidence': round(confidence, 2),
            'all_predictions': all_predictions
        })
    
    except Exception as e:
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({'error': f'Prediction error: {str(e)}'}), 500

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

# Load model at module level so it works with Gunicorn
print("Loading model...")
load_model_weights()
gc.collect()

if __name__ == '__main__':
    print("Starting Flask application...")
    # Use environment variable for port (required for deployment platforms)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

