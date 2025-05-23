from setuptools import setup

APP = ['main.py']
DATA_FILES = ['tray_icon.png']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pystray', 'PIL', 'pyperclip', 'dotenv'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
