#!/bin/bash

echo "📦 Installing AIImageTokenSaver..."

# Install dependencies
sudo apt update
sudo apt install -y python3 python3-pip xclip flameshot

# Install Python libraries
pip3 install --user pillow pyperclip pystray python-dotenv

# Create project directory
mkdir -p ~/AIImageTokenSaver/src
cd ~/AIImageTokenSaver

# Download main.py and required files
curl -O https://raw.githubusercontent.com/anombyte/AIImageTokenSaver/main/main.py
curl -O https://raw.githubusercontent.com/anombyte/AIImageTokenSaver/main/tray_icon.png

# Download all src modules
cd src
curl -O https://raw.githubusercontent.com/anombyte/AIImageTokenSaver/main/src/config.py
curl -O https://raw.githubusercontent.com/anombyte/AIImageTokenSaver/main/src/clipboard.py
curl -O https://raw.githubusercontent.com/anombyte/AIImageTokenSaver/main/src/startup.py
curl -O https://raw.githubusercontent.com/anombyte/AIImageTokenSaver/main/src/uninstall.py
curl -O https://raw.githubusercontent.com/anombyte/AIImageTokenSaver/main/src/tray.py

cd ..

# Create .desktop autostart entry (GNOME only)
cat <<EOF > ~/.config/autostart/ai-image-token-saver.desktop
[Desktop Entry]
Name=AIImageTokenSaver
Comment=Auto image optimizer for Claude API
Exec=python3 $HOME/AIImageTokenSaver/main.py
Icon=$HOME/AIImageTokenSaver/tray_icon.png
Terminal=false
Type=Application
X-GNOME-Autostart-enabled=true
EOF

echo "✅ Installed! Run it with: python3 ~/AIImageTokenSaver/main.py"
