@echo off
echo Installing Python dependencies...
pip install pillow pyperclip pystray python-dotenv
echo Running AIImageTokenSaver...
python main.py
pause
