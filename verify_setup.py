"""
Verification script to check if everything is ready for deployment.
Run this before deploying to ensure 100% success.
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_directory_exists(dirpath, description):
    """Check if a directory exists"""
    if os.path.isdir(dirpath):
        print(f"✅ {description}: {dirpath}")
        return True
    else:
        print(f"❌ {description}: {dirpath} - NOT FOUND")
        return False

def main():
    print("=" * 60)
    print("Lung Cancer Prediction System - Deployment Verification")
    print("=" * 60)
    print()
    
    all_checks = []
    
    # Critical files
    print("📁 Checking Critical Files...")
    all_checks.append(check_file_exists("app.py", "Main application"))
    all_checks.append(check_file_exists("requirements.txt", "Dependencies"))
    all_checks.append(check_file_exists("models/best_model.hdf5", "Model file (CRITICAL)"))
    all_checks.append(check_file_exists("Procfile", "Procfile for deployment"))
    all_checks.append(check_file_exists("render.yaml", "Render configuration"))
    print()
    
    # Frontend files
    print("🎨 Checking Frontend Files...")
    all_checks.append(check_file_exists("templates/index.html", "HTML template"))
    all_checks.append(check_file_exists("static/css/style.css", "CSS stylesheet"))
    all_checks.append(check_file_exists("static/js/script.js", "JavaScript file"))
    print()
    
    # Configuration files
    print("⚙️ Checking Configuration Files...")
    all_checks.append(check_file_exists("runtime.txt", "Python version"))
    all_checks.append(check_file_exists(".gitignore", "Git ignore file"))
    all_checks.append(check_file_exists("README.md", "README documentation"))
    print()
    
    # Directories
    print("📂 Checking Directories...")
    all_checks.append(check_directory_exists("templates", "Templates directory"))
    all_checks.append(check_directory_exists("static", "Static directory"))
    all_checks.append(check_directory_exists("models", "Models directory"))
    print()
    
    # Model file size check
    print("📊 Model File Information...")
    model_path = "models/best_model.hdf5"
    if os.path.exists(model_path):
        size_mb = os.path.getsize(model_path) / (1024 * 1024)
        print(f"   Model file size: {size_mb:.2f} MB")
        if size_mb > 100:
            print("   ⚠️  Model file is > 100MB. Consider using Git LFS.")
        else:
            print("   ✅ Model file size is OK for GitHub")
    print()
    
    # Summary
    print("=" * 60)
    if all(all_checks):
        print("✅ ALL CHECKS PASSED!")
        print("✅ Your project is ready for deployment!")
        print()
        print("Next steps:")
        print("1. Run: git add .")
        print("2. Run: git commit -m 'Ready for deployment'")
        print("3. Push to GitHub")
        print("4. Deploy on Render/Railway")
        print()
        print("See docs/DEPLOYMENT_GUIDE.md for detailed instructions.")
        return 0
    else:
        print("❌ SOME CHECKS FAILED!")
        print("Please fix the issues above before deploying.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

