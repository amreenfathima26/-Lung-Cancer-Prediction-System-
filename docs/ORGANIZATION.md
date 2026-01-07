# Project Organization

This document explains the folder structure and organization of the Lung Cancer Prediction System.

## 📁 Folder Structure

```
lung-cancer-prediction/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── Procfile                  # Deployment configuration
├── runtime.txt               # Python version
├── setup.py                  # Setup script
├── .gitignore               # Git ignore rules
├── README.md                 # Main project documentation (GitHub)
│
├── data/                     # 📸 ALL IMAGES AND DATASETS
│   ├── test_images/         # Sample test images for quick testing
│   ├── *.png                # Loose image files
│   └── Lung-Cancer-.../     # Original dataset folder
│       └── dataset/         # Full dataset (train/test/valid)
│
├── models/                   # 🤖 MODEL FILES
│   └── best_model.hdf5      # Trained model weights
│
├── docs/                     # 📚 DOCUMENTATION
│   ├── README.md            # Full documentation
│   ├── DEPLOYMENT.md        # Deployment guide
│   ├── QUICKSTART.md        # Quick start guide
│   ├── PROJECT_STRUCTURE.md # Project structure details
│   └── ORGANIZATION.md      # This file
│
├── static/                   # 🎨 FRONTEND ASSETS
│   ├── css/
│   │   └── style.css        # Stylesheet
│   └── js/
│       └── script.js        # JavaScript
│
├── templates/                # 📄 HTML TEMPLATES
│   └── index.html           # Main web page
│
└── uploads/                  # 📤 TEMPORARY UPLOADS (auto-created)
    └── (deleted after prediction)
```

## 📂 Folder Purposes

### Root Directory (`/`)
**Purpose**: Contains only essential code and configuration files
- `app.py` - Main application
- `requirements.txt` - Dependencies
- `Procfile` - Deployment config
- `README.md` - GitHub documentation

### `data/` Folder
**Purpose**: All images, datasets, and image-related files
- Test images for quick testing
- Original dataset folders
- Any loose image files
- **Keep all images here!**

### `models/` Folder
**Purpose**: Machine learning model files
- `best_model.hdf5` - Trained model weights
- Future model versions can go here

### `docs/` Folder
**Purpose**: All documentation files
- Detailed guides
- Project documentation
- Deployment instructions
- **Note**: `README.md` is also in root for GitHub visibility

### `static/` Folder
**Purpose**: Frontend static assets
- CSS stylesheets
- JavaScript files
- Images used in the web interface (if any)

### `templates/` Folder
**Purpose**: HTML templates for Flask
- Web page templates
- Jinja2 templates

### `uploads/` Folder
**Purpose**: Temporary file storage
- Created automatically
- Stores uploaded images temporarily
- Files are deleted after prediction

## 🎯 Organization Rules

1. **Images** → Always go in `data/` folder
2. **Code** → Keep in root or appropriate subfolders
3. **Documentation** → Goes in `docs/` (except README.md in root)
4. **Models** → Go in `models/` folder
5. **Temporary files** → Go in `uploads/` (auto-created)

## 📝 File Naming Conventions

- **Code files**: Use lowercase with underscores (`app.py`, `setup.py`)
- **Documentation**: Use UPPERCASE (`README.md`, `DEPLOYMENT.md`)
- **Images**: Descriptive names (`test_normal_1.png`)
- **Models**: Clear versioning (`best_model.hdf5`)

## 🔄 Adding New Files

### Adding Images
```bash
# Move to data folder
move new_image.png data/
```

### Adding Documentation
```bash
# Move to docs folder
move new_doc.md docs/
```

### Adding Models
```bash
# Copy to models folder
copy new_model.h5 models/
```

## ✅ Benefits of This Organization

1. **Clean Root**: Easy to find main files
2. **Separated Concerns**: Images separate from code
3. **Easy Navigation**: Clear folder purposes
4. **Git-Friendly**: Can ignore large image folders easily
5. **Professional**: Standard project structure

## 🚀 Deployment Notes

- The app automatically looks for models in `models/` folder
- Test images are in `data/test_images/` for easy access
- Documentation is organized but README.md stays in root for GitHub

---

**Last Updated**: Project reorganization complete
**Maintained By**: Project structure follows Flask best practices

