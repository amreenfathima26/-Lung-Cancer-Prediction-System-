"""
Setup script for Lung Cancer Prediction System
Run this script to set up the project for the first time.
"""

import os
import subprocess
import sys

def create_directories():
    """Create necessary directories"""
    directories = ['uploads', 'templates', 'static/css', 'static/js']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✓ Created directory: {directory}")

def check_model_file():
    """Check if model file exists"""
    possible_paths = [
        'best_model.hdf5',
        'Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main (1)/Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main/best_model.hdf5',
        'Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main/Lung-Cancer-Prediction-using-CNN-and-Transfer-Learning-main/best_model.hdf5'
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            print(f"✓ Found model file at: {path}")
            return True
    
    print("⚠ Warning: Model file (best_model.hdf5) not found!")
    print("  The application will not work without the model file.")
    print("  Please ensure best_model.hdf5 exists in the project directory.")
    return False

def install_dependencies():
    """Install Python dependencies"""
    print("\nInstalling dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        return False

def main():
    print("=" * 50)
    print("Lung Cancer Prediction System - Setup")
    print("=" * 50)
    print()
    
    # Create directories
    print("Creating directories...")
    create_directories()
    print()
    
    # Check model file
    print("Checking for model file...")
    model_exists = check_model_file()
    print()
    
    # Install dependencies
    install_dependencies()
    print()
    
    print("=" * 50)
    if model_exists:
        print("Setup complete! You can now run: python app.py")
    else:
        print("Setup complete, but model file is missing!")
        print("Please add best_model.hdf5 before running the application.")
    print("=" * 50)

if __name__ == "__main__":
    main()

