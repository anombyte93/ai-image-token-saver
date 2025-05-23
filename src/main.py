# main.py (modularized AIImageTokenSaver launcher)

from src.config import MAX_WIDTH, WEBP_QUALITY, TOKEN_COST_PER_1K, stats
from src.clipboard import monitor_clipboard
from src.tray import create_icon
from src.startup import add_to_startup

import threading


def run():
    t = threading.Thread(target=monitor_clipboard, daemon=True)
    t.start()
    create_icon().run()


if __name__ == "__main__":
    add_to_startup()
    run()
