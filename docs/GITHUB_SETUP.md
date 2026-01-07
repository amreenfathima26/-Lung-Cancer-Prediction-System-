# 📦 GitHub Setup Guide

Complete guide to prepare your project for GitHub and deployment.

## Step 1: Initialize Git Repository

```bash
# Navigate to project directory
cd lung

# Initialize Git
git init

# Add all files
git add .

# Check what will be committed
git status
```

## Step 2: Create .gitattributes (For Large Files)

If your model file is large (>100MB), use Git LFS:

```bash
# Install Git LFS (if not installed)
# Windows: Download from https://git-lfs.github.com/
# Mac: brew install git-lfs
# Linux: sudo apt-get install git-lfs

# Initialize Git LFS
git lfs install

# Track model files
git lfs track "models/*.hdf5"
git lfs track "models/*.h5"

# Add .gitattributes
git add .gitattributes
```

## Step 3: First Commit

```bash
git commit -m "Initial commit: Lung Cancer Prediction System - Production Ready"
```

## Step 4: Create GitHub Repository

1. Go to [github.com](https://github.com)
2. Click "+" → "New repository"
3. Repository name: `lung-cancer-prediction` (or your choice)
4. Description: "AI-powered lung cancer classification system using CNN"
5. **Public** (for free deployment) or **Private**
6. **DO NOT** initialize with README (you already have one)
7. Click "Create repository"

## Step 5: Connect and Push

```bash
# Add remote (replace YOUR_USERNAME and YOUR_REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## Step 6: Verify Files on GitHub

Check that these files are on GitHub:
- ✅ `app.py`
- ✅ `requirements.txt`
- ✅ `models/best_model.hdf5` (most important!)
- ✅ `templates/index.html`
- ✅ `static/css/style.css`
- ✅ `static/js/script.js`
- ✅ `README.md`
- ✅ `Procfile`
- ✅ `render.yaml`

## Step 7: Enable GitHub Actions (Optional)

The `.github/workflows/deploy.yml` file will automatically:
- Test your code on push
- Verify model file exists
- Check dependencies

## Important Notes

### Model File Size

If `best_model.hdf5` is > 100MB:
- Use Git LFS (see Step 2)
- Or host model separately and download on deployment

### What NOT to Commit

These are in `.gitignore`:
- `uploads/` folder
- `__pycache__/`
- `venv/`
- Dataset images in `data/`
- But **DO commit** `models/best_model.hdf5`

### Verify Model File

```bash
# Check if model file is tracked
git ls-files | grep best_model.hdf5

# Should show: models/best_model.hdf5
```

## Next Steps

After GitHub setup:
1. Follow [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
2. Deploy to Render/Railway
3. Get free domain
4. Test your live app!

---

**Status**: Ready for GitHub and deployment! 🚀

