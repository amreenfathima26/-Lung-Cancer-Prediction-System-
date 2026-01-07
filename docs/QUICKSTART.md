# Quick Start Guide

Get your Lung Cancer Prediction System up and running in minutes!

## 🚀 Quick Setup (5 minutes)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or use the setup script:

```bash
python setup.py
```

### Step 2: Verify Model File

Make sure `best_model.hdf5` exists. The app will look for it in:
- Root directory: `best_model.hdf5`
- Subdirectory: `Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main (1)/Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main/best_model.hdf5`

### Step 3: Run the Application

```bash
python app.py
```

### Step 4: Open in Browser

Navigate to: `http://localhost:5000`

## 📝 Testing the Application

1. **Upload an image:**
   - Click the upload area or drag & drop
   - Supported formats: PNG, JPG, JPEG
   - Max file size: 16MB

2. **Get predictions:**
   - Click "Analyze Image"
   - View results with confidence scores

3. **Try different images:**
   - Click "Change Image" to upload another

## 🐛 Troubleshooting

### "Model not loaded" error

- Check if `best_model.hdf5` exists in the project
- Verify the file path in `app.py` matches your structure
- Ensure you have TensorFlow installed: `pip install tensorflow`

### Port already in use

Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use port 5001 instead
```

### Import errors

Make sure all dependencies are installed:
```bash
pip install --upgrade -r requirements.txt
```

### Slow first prediction

This is normal! The model loads on the first prediction. Subsequent predictions will be faster.

## 📦 For GitHub Deployment

1. **Initialize Git repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create GitHub repository:**
   - Go to GitHub and create a new repository
   - Don't initialize with README (you already have one)

3. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git branch -M main
   git push -u origin main
   ```

4. **Deploy to platform:**
   - See [DEPLOYMENT.md](DEPLOYMENT.md) for platform-specific instructions
   - Recommended: Render (easiest setup)

## ✅ Checklist

Before deploying, ensure:

- [ ] All dependencies installed
- [ ] Model file (`best_model.hdf5`) exists
- [ ] Application runs locally without errors
- [ ] Tested with sample images
- [ ] All files committed to Git
- [ ] README.md updated (if needed)

## 🎯 Next Steps

- Read [README.md](README.md) for full documentation
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment options
- Customize the UI in `static/css/style.css`
- Add features as needed

---

**Need help?** Open an issue on GitHub or check the documentation.

