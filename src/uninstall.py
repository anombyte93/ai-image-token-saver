
import os
import platform
import sys
import shutil
import subprocess

def uninstall():
    try:
        # 1. Remove logs and config
        config_path = os.path.expanduser("~/.ai_image_token_saver/")
        if os.path.exists(config_path):
            shutil.rmtree(config_path)

        # 2. Remove autostart entries
        if platform.system() == "Windows":
            import winshell
            shortcut = os.path.join(winshell.startup(), "AIImageTokenSaver.lnk")
            if os.path.exists(shortcut):
                os.remove(shortcut)
        elif platform.system() == "Linux":
            desktop_entry = os.path.expanduser("~/.config/autostart/ai-image-token-saver.desktop")
            if os.path.exists(desktop_entry):
                os.remove(desktop_entry)

        # 3. Uninstall packages
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y",
                        "pillow", "pyperclip", "pystray", "python-dotenv"])

        # 4. Confirmation popup for tray mode
        try:
            from tkinter import messagebox, Tk
            root = Tk()
            root.withdraw()
            messagebox.showinfo("AIImageTokenSaver", "✅ Uninstall complete. You may delete the file manually.")
        except Exception:
            print("✅ Uninstall complete.")

    except Exception as e:
        print(f"❌ Error during uninstall: {e}")

if __name__ == "__main__":
    uninstall()
