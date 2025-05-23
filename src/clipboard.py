# src/clipboard.py

import time
import io
import base64
import json
import pyperclip
from PIL import ImageGrab, Image
from src.config import MAX_WIDTH, WEBP_QUALITY, TOKEN_COST_PER_1K, stats, save_stats


def resize_image(image: Image.Image) -> Image.Image:
    width, height = image.size
    if width <= MAX_WIDTH:
        return image
    new_height = int((MAX_WIDTH / width) * height)
    return image.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)


def encode_image_to_base64(image: Image.Image, format="WEBP", quality=WEBP_QUALITY) -> (str, int):
    buffer = io.BytesIO()
    image.save(buffer, format=format, quality=quality)
    byte_data = buffer.getvalue()
    base64_string = base64.b64encode(byte_data).decode("utf-8")
    return base64_string, len(base64_string)


def estimate_tokens(base64_len: int) -> int:
    return int(base64_len / 4)


def generate_payload(b64: str) -> str:
    return json.dumps({
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/webp",
            "data": b64
        }
    }, indent=2)


def monitor_clipboard():
    last_image = None
    while True:
        try:
            image = ImageGrab.grabclipboard()
            if isinstance(image, Image.Image) and image != last_image:
                last_image = image
                resized = resize_image(image)

                b64_orig, len_orig = encode_image_to_base64(image, format="PNG")
                b64_resized, len_resized = encode_image_to_base64(resized)

                tokens_orig = estimate_tokens(len_orig)
                tokens_resized = estimate_tokens(len_resized)
                saved_tokens = tokens_orig - tokens_resized

                stats["original_tokens"] += tokens_orig
                stats["optimized_tokens"] += tokens_resized

                payload = generate_payload(b64_resized)
                pyperclip.copy(payload)

                print(f"\n🖼️ Optimized image detected!")
                print(f"📦 Original tokens: {tokens_orig:,}")
                print(f"📉 Resized tokens:  {tokens_resized:,}")
                print(f"💸 Saved tokens:    {saved_tokens:,} (~${saved_tokens / 1000 * TOKEN_COST_PER_1K:.4f})")

                save_stats()
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)