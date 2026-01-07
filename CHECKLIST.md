# ✅ Pre-Deployment Checklist

Use this checklist to ensure your deployment works 100%.

## Before GitHub

- [ ] All code files are in place
- [ ] `models/best_model.hdf5` exists
- [ ] Tested locally: `python app.py` works
- [ ] Can upload images and get predictions
- [ ] All dependencies in `requirements.txt`

## GitHub Setup

- [ ] Git repository initialized
- [ ] All files added: `git add .`
- [ ] Model file is tracked: `git ls-files | grep best_model.hdf5`
- [ ] Committed: `git commit -m "Initial commit"`
- [ ] GitHub repository created
- [ ] Remote added: `git remote add origin ...`
- [ ] Pushed to GitHub: `git push -u origin main`
- [ ] Verified files on GitHub (especially model file)

## Deployment

- [ ] Chosen deployment platform (Render/Railway)
- [ ] Connected GitHub repository
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn app:app`
- [ ] Deployment successful
- [ ] Health check passes: `/health` endpoint
- [ ] Can access main page
- [ ] Can upload and predict images

## Post-Deployment

- [ ] Tested with sample images
- [ ] Predictions work correctly
- [ ] Custom domain configured (optional)
- [ ] HTTPS enabled (automatic on most platforms)

## Troubleshooting

If something doesn't work:

1. **Model not loading?**
   - Check if `models/best_model.hdf5` is in Git
   - Verify file path in `app.py`

2. **Build fails?**
   - Check `requirements.txt`
   - Verify Python version in `runtime.txt`

3. **App crashes?**
   - Check deployment logs
   - Verify PORT environment variable

4. **Predictions fail?**
   - Check model file exists
   - Verify image upload works
   - Check error logs

## Success Criteria

✅ Health endpoint returns: `{"status": "healthy", "model_loaded": true}`
✅ Can upload images
✅ Predictions return results
✅ No errors in logs

---

**Status**: Check all items for 100% working deployment!

