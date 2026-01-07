# Deployment Guide

This guide will help you deploy the Lung Cancer Prediction System to various platforms.

## Quick Start

1. **Ensure all files are in place:**
   - `app.py` - Flask application
   - `best_model.hdf5` - Trained model (must be in root or subdirectory)
   - `requirements.txt` - Dependencies
   - `Procfile` - For Heroku/Railway
   - `templates/` and `static/` directories

2. **Test locally first:**
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

3. **Choose a deployment platform** (see below)

## Platform-Specific Instructions

### 🚀 Render (Easiest - Recommended)

1. Go to [render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: lung-cancer-prediction (or your choice)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click "Create Web Service"
6. Wait for deployment (first time takes ~5-10 minutes)

**Note**: Render has a free tier with some limitations.

### 🚀 Heroku

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

**Note**: Heroku free tier was discontinued, but paid plans start at $5/month.

### 🚀 Railway

1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway auto-detects Python and deploys
5. Add environment variables if needed (none required for basic setup)

**Note**: Railway offers $5 free credit monthly.

### 🚀 PythonAnywhere

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your files via Files tab
3. Create a new Web App
4. Configure WSGI file to point to your Flask app
5. Reload the web app

### 🚀 Local Network Deployment

For testing on your local network:

1. Find your IP address:
   - Windows: `ipconfig` (look for IPv4)
   - Mac/Linux: `ifconfig` or `ip addr`

2. Update `app.py`:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5000)
   ```

3. Run: `python app.py`
4. Access from other devices: `http://YOUR_IP:5000`

## Important Notes

### Model File Size

The `best_model.hdf5` file might be large (often 50-200MB+). Some platforms have file size limits:

- **GitHub**: 100MB file limit (use Git LFS for larger files)
- **Render/Heroku**: No strict limit, but large files slow deployment
- **Railway**: Handles large files well

### Using Git LFS for Model File

If your model file is > 100MB:

1. Install Git LFS: `git lfs install`
2. Track model file: `git lfs track "*.hdf5"`
3. Add to git: `git add .gitattributes best_model.hdf5`
4. Commit and push normally

### Environment Variables

Currently, no environment variables are required. If you add features like:
- Database connections
- API keys
- Secret keys

Add them in your platform's environment variable settings.

## Troubleshooting

### Model Not Loading

- Ensure `best_model.hdf5` is in the repository
- Check file path in `app.py` matches your structure
- Verify file permissions

### Build Fails

- Check Python version compatibility
- Ensure all dependencies in `requirements.txt` are correct
- Check platform logs for specific errors

### App Crashes

- Check application logs on your platform
- Verify model file is accessible
- Ensure uploads directory has write permissions

### Slow Predictions

- First prediction loads the model (slower)
- Consider using a GPU-enabled platform for faster inference
- Implement model caching if not already done

## Post-Deployment

1. **Test the deployment:**
   - Visit your app URL
   - Upload a test image
   - Verify predictions work

2. **Monitor:**
   - Check application logs regularly
   - Monitor resource usage
   - Set up error alerts if available

3. **Update:**
   - Push changes to GitHub
   - Platform will auto-deploy (if configured)
   - Or manually trigger deployment

## Security Considerations

- Add rate limiting for production
- Implement file size and type validation (already done)
- Consider adding authentication for sensitive use
- Use HTTPS (most platforms provide this automatically)
- Sanitize file uploads (already implemented)

## Cost Estimates

- **Render Free Tier**: Free (with limitations)
- **Heroku**: $5-7/month (basic)
- **Railway**: $5 free credit/month, then pay-as-you-go
- **PythonAnywhere**: Free tier available

---

For issues, check the main README.md or open an issue on GitHub.

