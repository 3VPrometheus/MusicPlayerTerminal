#!/bin/bash

for module in "pytube" "youtubesearchpython"

do
    pip install $module > nullpip.txt
    if [ $? -eq 0 ]; then
        echo "Successfully installed $module"
    else
        echo "Failed to install $module"
    fi
done