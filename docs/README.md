# 🫁 Lung Cancer Prediction System

A dynamic web application for lung cancer classification using Convolutional Neural Networks (CNN) and Transfer Learning. This system classifies lung CT scan images into four categories: Normal, Adenocarcinoma, Large Cell Carcinoma, and Squamous Cell Carcinoma.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- **Modern Web Interface**: Beautiful, responsive UI with drag-and-drop image upload
- **Real-time Predictions**: Instant classification results with confidence scores
- **Detailed Analysis**: View probabilities for all cancer types
- **Mobile Friendly**: Works seamlessly on desktop and mobile devices
- **Easy Deployment**: Ready to deploy on various platforms

## 📋 Table of Contents

- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Model Information](#model-information)
- [Technologies Used](#technologies-used)
- [Disclaimer](#disclaimer)
- [License](#license)

## 🚀 Demo

Upload a lung CT scan image and get instant predictions with confidence scores for all cancer types.

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lung-cancer-prediction.git
   cd lung-cancer-prediction
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model file exists**
   - Make sure `best_model.hdf5` is in the root directory
   - If you need to train the model, refer to the original training script

## 🎯 Usage

### Running Locally

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   - Navigate to `http://localhost:5000`
   - Upload a lung CT scan image (PNG, JPG, or JPEG)
   - Click "Analyze Image" to get predictions

### API Endpoint

You can also use the API directly:

```bash
curl -X POST -F "file=@your_image.png" http://localhost:5000/predict
```

Response:
```json
{
  "success": true,
  "prediction": "Normal",
  "confidence": 95.23,
  "all_predictions": {
    "Normal": 95.23,
    "Adenocarcinoma": 2.15,
    "Large Cell Carcinoma": 1.50,
    "Squamous Cell Carcinoma": 1.12
  }
}
```

## 📁 Project Structure

```
lung-cancer-prediction/
│
├── app.py                 # Flask application (main backend)
├── requirements.txt       # Python dependencies
├── .gitignore           # Git ignore file
├── README.md            # Project documentation
├── best_model.hdf5      # Trained model weights (ensure this exists)
│
├── templates/
│   └── index.html       # Main HTML template
│
├── static/
│   ├── css/
│   │   └── style.css    # Stylesheet
│   └── js/
│       └── script.js    # Frontend JavaScript
│
└── uploads/             # Temporary upload directory (auto-created)
```

## 🚢 Deployment

> **Note**: GitHub Pages only serves static websites. For this Flask application, you'll need to deploy to a platform that supports Python/Flask (Render, Heroku, Railway, etc.). See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

### Option 1: Render (Recommended)

1. **Create a Render account** at [render.com](https://render.com)

2. **Create a new Web Service**
   - Connect your GitHub repository
   - Select "Python" as the environment
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`

3. **Add Environment Variables** (if needed)
   - No special environment variables required for basic setup

4. **Deploy**
   - Render will automatically deploy your application

### Option 2: Heroku

1. **Install Heroku CLI** and login

2. **Create a Procfile**
   ```
   web: gunicorn app:app
   ```

3. **Deploy**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku create your-app-name
   git push heroku main
   ```

### Option 3: Railway

1. **Create a Railway account** at [railway.app](https://railway.app)

2. **Connect your GitHub repository**

3. **Railway will auto-detect Python and deploy**

### Option 4: Local Network

For testing on your local network:

```bash
python app.py
```

Then access from other devices on the same network using your computer's IP address.

## 🤖 Model Information

- **Architecture**: Xception (Transfer Learning)
- **Input Size**: 350x350 pixels
- **Classes**: 4 (Normal, Adenocarcinoma, Large Cell Carcinoma, Squamous Cell Carcinoma)
- **Training**: The model was trained using TensorFlow/Keras with data augmentation

### Model Training

If you need to retrain the model, refer to the original training script in the `Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main` directory.

## 🛠 Technologies Used

- **Backend**: Flask (Python web framework)
- **Deep Learning**: TensorFlow/Keras
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Image Processing**: Pillow, NumPy
- **Deployment**: Gunicorn (WSGI server)

## ⚠️ Disclaimer

**IMPORTANT**: This tool is for **educational and research purposes only**. It should **NOT** be used as a substitute for professional medical diagnosis, treatment, or advice. Always consult with qualified healthcare professionals for medical decisions.

- This system is not FDA approved
- Results may not be 100% accurate
- Do not use for actual medical diagnosis
- Always seek professional medical advice

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Dataset: [Chest CT Scan Images Dataset](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images) on Kaggle
- TensorFlow team for the Xception model
- All contributors to the open-source libraries used

## 📧 Contact

For questions or issues, please open an issue on GitHub.

---

**Made with ❤️ for medical research and education**

