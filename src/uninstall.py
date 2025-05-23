# src/startup.py

def add_to_startup():
    import platform
    import os

    if platform.system() == "Windows":
        try:
            import winshell
            from win32com.client import Dispatch
            import sys

            startup_path = winshell.startup()
            shortcut_path = os.path.join(startup_path, "AIImageTokenSaver.lnk")
            target = sys.executable
            script = os.path.abspath(__file__)

            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortcut(shortcut_path)
            shortcut.TargetPath = target
            shortcut.Arguments = f'"{script}"'
            shortcut.WorkingDirectory = os.path.dirname(script)
            shortcut.IconLocation = os.path.join(os.path.dirname(script), "../tray_icon.ico")
            shortcut.save()
        except Exception as e:
            print(f"[!] Failed to add to startup: {e}")

    elif platform.system() == "Linux":
        try:
            autostart_dir = os.path.expanduser("~/.config/autostart")
            os.makedirs(autostart_dir, exist_ok=True)
            desktop_path = os.path.join(autostart_dir, "ai-image-token-saver.desktop")
            with open(desktop_path, "w") as f:
                f.write("""
[Desktop Entry]
Name=AIImageTokenSaver
Comment=Auto image optimizer for Claude API
Exec=python3 ~/AIImageTokenSaver/main.py
Icon=~/AIImageTokenSaver/tray_icon.png
Terminal=false
Type=Application
X-GNOME-Autostart-enabled=true
""")
        except Exception as e:
            print(f"[!] Failed to create autostart entry: {e}")