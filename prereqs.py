# This script creates any necessary file/directories and installs any necessary packages
# Please run this script before running MusicPlayerTerm.py

# Import modules. If a module is not found, install it

def get_prereqs():
    import os
    modules = ["pytube", "youtubesearchpython", "moviepy"]

    for module in modules:
        try:
            exec(f"import {module}")
        except ImportError:
            print(f"Module {module} not found. Installing...")
            os.system(f"pip install {module}")

    # Create the necessary directories
    directories = ["/data/data/com.termux/files/home/Music", "/storage/emulated/0/Music"]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)