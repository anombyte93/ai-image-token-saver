# src/config.py

import os
import json

CONFIG_FILE = os.path.expanduser("~/.ai_image_token_saver/config.json")
LOG_FILE = os.path.expanduser("~/.ai_image_token_saver/log.json")

# Load user-defined profiles and hotkeys
DEFAULT_PROFILES = {
    "LLM": {"width": 512, "quality": 70},
    "Claude": {"width": 640, "quality": 80},
    "Custom": {"width": 640, "quality": 80},
}

DEFAULT_HOTKEYS = {
    "Super+Shift+S": "LLM"
}


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"hotkeys": DEFAULT_HOTKEYS, "profiles": DEFAULT_PROFILES}


def save_config(config):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)


config = load_config()
HOTKEYS = config["hotkeys"]
PROFILES = config["profiles"]


def load_stats():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return {"original_tokens": 0, "optimized_tokens": 0}


def save_stats(stats):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        json.dump(stats, f)


stats = load_stats()
