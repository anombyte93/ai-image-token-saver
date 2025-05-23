# src/tray.py

from pystray import Icon, MenuItem, Menu
from PIL import Image as PILImage
import os
from src.config import TOKEN_COST_PER_1K, stats
from /gui import launch_gui


def get_tooltip():
    saved_tokens = stats["original_tokens"] - stats["optimized_tokens"]
    saved_dollars = saved_tokens / 1000 * TOKEN_COST_PER_1K
    return f"Saved {saved_tokens:,} tokens (~${saved_dollars:.2f})"


def confirm_uninstall():
    import tkinter
    from tkinter import messagebox
    from src.uninstall import uninstall

    root = tkinter.Tk()
    root.withdraw()
    if messagebox.askyesno("Uninstall AIImageTokenSaver", "Are you sure you want to uninstall this app?"):
        uninstall()


def create_icon():
    icon_path = os.path.join(os.path.dirname(__file__), "../tray_icon.png")
    image = PILImage.open(icon_path)
    return Icon("AIImageTokenSaver", image, "AIImageTokenSaver", menu=Menu(
        MenuItem(lambda: get_tooltip(), None, enabled=False),
        MenuItem("Uninstall", lambda icon, item: confirm_uninstall()),
        MenuItem("Quit", lambda icon, item: icon.stop())
        MenuItem("Configure", lambda icon, item: launch_gui()),
    ))