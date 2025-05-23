# 🖼 AIImageTokenSaver

The cutest Claude image optimizer — compress clipboard screenshots to save tokens and money in Claude API.

## ✨ Features

- 📋 Auto-detects clipboard screenshots (Win/Linux/macOS)
- 📐 Compresses to WebP + resizes for Claude
- 💸 Shows token + cost savings in tray hover
- 📎 JSON payload copied to clipboard (Claude-ready)
- 🖱 Right-click tray icon → Configure hotkeys
- 🔧 GUI to manage multiple screenshot profiles
- 🧠 Launches on startup, runs quietly in tray

---

## 🔧 Installation

### 🪟 Windows

One-liner (PowerShell):

Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/anombyte93/AIImageTokenSaver/main/setup.ps1 | Invoke-Expression

Or manually run `setup.bat` or download:

[⬇ Download AIImageTokenSaver.exe](https://github.com/anombyte93/AIImageTokenSaver/releases/latest/download/AIImageTokenSaver.exe)

---

### 🐧 Linux

Run this in terminal:

```bash
<(curl -s https://raw.githubusercontent.com/anombyte93/AIImageTokenSaver/main/install.sh)
```

Or download the binary manually:

[⬇ Download Linux binary](https://github.com/anombyte93/AIImageTokenSaver/releases/latest/download/main)

---

### 🍏 macOS

Run this in terminal:

```bash
<(curl -s https://raw.githubusercontent.com/anombyte93/AIImageTokenSaver/main/install_mac.sh)
```

Or download the `.dmg` or `.pkg`:

[⬇ Download macOS Installer](https://github.com/anombyte93/AIImageTokenSaver/releases/latest)

---

## 🧪 Developer Setup

````bash
git clone https://github.com/anombyte93/AIImageTokenSaver.git
cd AIImageTokenSaver
pip install -r requirements.txt
python main.py```

---

## 🧼 Uninstalling

- Right-click tray icon → Uninstall → Confirm
- Removes:
  - Local logs/config: `~/.ai_image_token_saver/`
  - System shortcut/startup entry
  - Installed Python packages (if installed via script)

---

## 📈 Coming Soon

- Token savings graph (weekly/monthly)
- Claude API integration
- Theme support & auto-updates

---

## ☕ Support Development

[Buy me a coffee →](https://buymeacoffee.com/anombyte93)

---

## 🔒 License

MIT — Free to use, modify, and redistribute. Credit appreciated 💚
````
