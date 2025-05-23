#!/bin/bash

echo "📦 Installing AIImageTokenSaver for macOS..."

# Download latest DMG or PKG from GitHub Releases
cd /tmp
curl -LO https://github.com/anombyte/AIImageTokenSaver/releases/latest/download/AIImageTokenSaver.dmg

# Mount the DMG
hdiutil attach AIImageTokenSaver.dmg

# Optional: copy to Applications
echo "🧩 Drag the app to /Applications or run it directly."

# Open mounted volume
open /Volumes/AIImageTokenSaver

echo "✅ Installer opened. Follow instructions to finish setup."
