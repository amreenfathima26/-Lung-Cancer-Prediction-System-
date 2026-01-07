# Project Structure

This document outlines the complete structure of the Lung Cancer Prediction System web application.

## 📁 Directory Structure

```
lung-cancer-prediction/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── Procfile                        # Heroku/Railway deployment config
├── runtime.txt                     # Python version specification
├── setup.py                        # Setup script for first-time setup
├── .gitignore                      # Git ignore rules
│
├── README.md                       # Main project documentation
├── DEPLOYMENT.md                   # Detailed deployment guide
├── QUICKSTART.md                   # Quick start guide
├── PROJECT_STRUCTURE.md            # This file
│
├── templates/                      # HTML templates
│   └── index.html                 # Main web page
│
├── static/                         # Static assets
│   ├── css/
│   │   └── style.css             # Stylesheet
│   └── js/
│       └── script.js             # Frontend JavaScript
│
├── uploads/                        # Temporary upload directory (auto-created)
│
├── .github/                        # GitHub configuration
│   └── workflows/
│       └── deploy.yml            # GitHub Actions workflow
│
└── best_model.hdf5                 # Trained model (should be in root or subdirectory)
```

## 📄 File Descriptions

### Core Application Files

- **app.py**: Flask backend application
  - Handles image uploads
  - Loads and uses the trained model
  - Provides REST API endpoints
  - Manages file uploads and predictions

- **requirements.txt**: Python package dependencies
  - Flask: Web framework
  - TensorFlow: Deep learning framework
  - NumPy: Numerical computing
  - Pillow: Image processing
  - Gunicorn: WSGI server for production

### Configuration Files

- **Procfile**: Tells Heroku/Railway how to run the app
- **runtime.txt**: Specifies Python version for deployment
- **.gitignore**: Excludes unnecessary files from Git

### Documentation Files

- **README.md**: Main project documentation with features, installation, and usage
- **DEPLOYMENT.md**: Detailed deployment instructions for various platforms
- **QUICKSTART.md**: Quick setup guide for getting started
- **PROJECT_STRUCTURE.md**: This file - explains project organization

### Frontend Files

- **templates/index.html**: Main HTML page with upload interface
- **static/css/style.css**: Modern, responsive styling
- **static/js/script.js**: Client-side JavaScript for interactivity

### Setup & Utilities

- **setup.py**: Automated setup script for first-time installation

## 🔄 Data Flow

1. **User uploads image** → Frontend (JavaScript)
2. **Image sent to server** → POST /predict endpoint
3. **Server processes image** → Flask app (app.py)
4. **Model makes prediction** → TensorFlow model
5. **Results returned** → JSON response
6. **Results displayed** → Frontend updates UI

## 🎯 Key Features by File

### app.py
- Image upload handling
- Model loading and inference
- Error handling
- API endpoints

### index.html
- Upload interface
- Image preview
- Results display
- Responsive design

### style.css
- Modern gradient design
- Mobile responsiveness
- Animations and transitions
- Professional medical UI

### script.js
- Drag & drop functionality
- File validation
- API communication
- Dynamic UI updates

## 📦 Dependencies

### Backend
- Flask 3.0.0
- TensorFlow 2.15.0
- NumPy 1.24.3
- Pillow 10.1.0
- Werkzeug 3.0.1

### Frontend
- Vanilla JavaScript (no frameworks)
- Modern CSS3
- HTML5

## 🚀 Deployment Files

- **Procfile**: For Heroku/Railway
- **runtime.txt**: Python version
- **.github/workflows/deploy.yml**: GitHub Actions CI/CD

## 📝 Notes

- The `uploads/` directory is created automatically
- Model file can be in root or subdirectory (app.py checks multiple locations)
- All uploaded images are automatically deleted after prediction
- The application is designed to be stateless (no database required)

## 🔒 Security Considerations

- File type validation
- File size limits (16MB)
- Secure filename handling
- No persistent file storage
- Input sanitization

---

For more information, see the main [README.md](README.md).

