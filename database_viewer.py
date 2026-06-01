# setup_client_server_fixed.py
# Fixed setup script without Unicode characters

import os
import subprocess
import sys
import shutil

def check_python_version():
    """Check if Python version is compatible"""
    print("Checking Python version...")
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        return False
    print(f"Python {sys.version_info.major}.{sys.version_info.minor} detected - OK")
    return True

def install_required_packages():
    """Install required Python packages"""
    print("\nInstalling required packages...")
    
    packages = [
        'watchdog',
        'pefile', 
        'joblib',
        'pandas',
        'numpy',
        'scikit-learn'
    ]
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                         check=True, capture_output=True)
            print(f"SUCCESS: {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Failed to install {package}: {e}")
            return False
    
    return True

def create_directory_structure():
    """Create required directory structure"""
    print("\nCreating directory structure...")
    
    directories = [
        "C:\\RansomwareDetector",
        "C:\\RansomwareDetector\\server",
        "C:\\RansomwareDetector\\client"
    ]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"SUCCESS: Created {directory}")
        except Exception as e:
            print(f"ERROR: Failed to create {directory}: {e}")
            return False
    
    return True

def check_model_file():
    """Check if model file exists"""
    print("\nChecking for model file...")
    
    model_path = "C:\\RansomwareDetector\\ransomware_lgb_model_optimized_final.joblib"
    
    if os.path.exists(model_path):
        print(f"SUCCESS: Model found at {model_path}")
        return True
    else:
        print(f"WARNING: Model not found at {model_path}")
        print("Please ensure your trained model is placed in the correct location")
        return False

def create_start_scripts():
    """Create convenient start scripts"""
    print("\nCreating start scripts...")
    
    # Server start script
    server_script = '''@echo off
echo Starting Ransomware Detection Server...
echo ======================================
cd C:\\RansomwareDetector\\server
python ransomware_detection_server.py
pause
'''
    
    # Client start script  
    client_script = '''@echo off
echo Starting Ransomware Detection Client...
echo ======================================
cd C:\\RansomwareDetector\\client
python ransomware_detection_client.py
pause
'''
    
    try:
        with open("C:\\RansomwareDetector\\server\\start_server.bat", 'w') as f:
            f.write(server_script)
        print("SUCCESS: Server start script created")
        
        with open("C:\\RansomwareDetector\\client\\start_client.bat", 'w') as f:
            f.write(client_script)
        print("SUCCESS: Client start script created")
        
        return True
    except Exception as e:
        print(f"ERROR: Failed to create start scripts: {e}")
        return False

def create_test_script():
    """Create a test script to verify setup"""
    test_script = '''# test_setup.py
# Test script to verify client-server setup

import socket
import json
import time
import os

def test_server_connection():
    """Test if server is reachable"""
    print("Testing server connection...")
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)
        client_socket.connect(('localhost', 8888))
        client_socket.close()
        print("SUCCESS: Server is reachable")
        return True
    except Exception as e:
        print(f"ERROR: Cannot connect to server: {e}")
        return False

def test_feature_extraction():
    """Test PE feature extraction"""
    print("Testing feature extraction...")
    
    try:
        import pefile
        print("SUCCESS: pefile import successful")
        return True
    except ImportError as e:
        print(f"ERROR: pefile import failed: {e}")
        return False

def test_model_loading():
    """Test model loading"""
    print("Testing model loading...")
    
    try:
        import joblib
        model_path = "C:\\\\RansomwareDetector\\\\ransomware_lgb_model_optimized_final.joblib"
        if not os.path.exists(model_path):
            print(f"ERROR: Model file not found: {model_path}")
            return False
            
        model = joblib.load(model_path)
        print("SUCCESS: Model loaded successfully")
        return True
    except Exception as e:
        print(f"ERROR: Model loading failed: {e}")
        return False

def main():
    print("RANSOMWARE DETECTION SYSTEM - SETUP TEST")
    print("="*50)
    
    tests = [
        ("Feature Extraction", test_feature_extraction),
        ("Model Loading", test_model_loading),
        ("Server Connection", test_server_connection)
    ]
    
    passed = 0
    for test_name, test_func in tests:
        print(f"\\n--- {test_name} ---")
        if test_func():
            passed += 1
    
    print(f"\\nTest Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("SUCCESS: All tests passed! System is ready.")
    else:
        print("WARNING: Some tests failed. Please fix issues before running.")

if __name__ == "__main__":
    main()
'''
    
    try:
        # Write with UTF-8 encoding to handle any special characters
        with open("C:\\RansomwareDetector\\test_setup.py", 'w', encoding='utf-8') as f:
            f.write(test_script)
        print("SUCCESS: Test script created")
        return True
    except Exception as e:
        print(f"ERROR: Failed to create test script: {e}")
        return False

def display_setup_instructions():
    """Display final setup instructions"""
    print("\n" + "="*60)
    print("SETUP COMPLETE!")
    print("="*60)
    print()
    print("Directory Structure:")
    print("   C:\\RansomwareDetector\\")
    print("   |-- server\\")
    print("   |   |-- ransomware_detection_server.py")
    print("   |   +-- start_server.bat")
    print("   |-- client\\")
    print("   |   |-- ransomware_detection_client.py")
    print("   |   +-- start_client.bat")
    print("   |-- ransomware_lgb_model_optimized_final.joblib")
    print("   +-- test_setup.py")
    print()
    print("How to Run:")
    print("   1. First, copy the server and client files to their respective folders")
    print("   2. Start the SERVER first:")
    print("      - Double-click: C:\\RansomwareDetector\\server\\start_server.bat")
    print("      - OR run: python C:\\RansomwareDetector\\server\\ransomware_detection_server.py")
    print()
    print("   3. Then start the CLIENT:")
    print("      - Double-click: C:\\RansomwareDetector\\client\\start_client.bat") 
    print("      - OR run: python C:\\RansomwareDetector\\client\\ransomware_detection_client.py")
    print()
    print("Testing:")
    print("   - Run test: python C:\\RansomwareDetector\\test_setup.py")
    print()
    print("Configuration:")
    print("   - Server runs on: localhost:8888")
    print("   - Database: C:\\RansomwareDetector\\server\\detections.db")
    print("   - Logs: ransomware_server.log & ransomware_client.log")
    print()
    print("What it monitors:")
    print("   - Downloads folder")
    print("   - Desktop")
    print("   - Documents")
    print("   - USB drives (D:, E:)")
    print("   - Temp folders")
    print("   - WhatsApp downloads (if available)")

def main():
    """Main setup function"""
    print("RANSOMWARE DETECTION SYSTEM - CLIENT-SERVER SETUP")
    print("="*60)
    print("This will set up a complete client-server ransomware detection system")
    print()
    
    setup_steps = [
        ("Checking Python version", check_python_version),
        ("Installing required packages", install_required_packages), 
        ("Creating directory structure", create_directory_structure),
        ("Checking model file", check_model_file),
        ("Creating start scripts", create_start_scripts),
        ("Creating test script", create_test_script)
    ]
    
    for step_name, step_func in setup_steps:
        print(f"\n--- {step_name} ---")
        if not step_func():
            print(f"ERROR: Setup failed at: {step_name}")
            return False
    
    display_setup_instructions()
    return True

if __name__ == "__main__":
    main()