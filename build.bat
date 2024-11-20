@echo off
pip install -r requirements.txt
pyinstaller --onefile generic_launcher.py -n generic_launcher
pause