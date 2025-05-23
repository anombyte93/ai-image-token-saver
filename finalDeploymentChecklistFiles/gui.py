import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import json
import os
from .config import CONFIG_FILE, load_config, save_config

class Configurator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AIImageTokenSaver Config")
        self.geometry("500x300")
        self.config = load_config()
        self.tree = None
        self.draw_gui()

    def draw_gui(self):
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        columns = ("Hotkey", "Width", "Quality")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Populate tree
        for hotkey, profile in self.config["hotkeys"].items():
            settings = self.config["profiles"][profile]
            self.tree.insert("", tk.END, values=(hotkey, settings["width"], settings["quality"]))

        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, pady=5)

        ttk.Button(btn_frame, text="Add", command=self.add_entry).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete", command=self.delete_entry).pack(side=tk.LEFT, padx=5)

    def add_entry(self):
        hotkey = simpledialog.askstring("Hotkey", "Enter hotkey (e.g., Ctrl+Alt+P):")
        width = simpledialog.askinteger("Width", "Enter max width:", minvalue=100, maxvalue=2000)
        quality = simpledialog.askinteger("Quality", "Enter quality (1-100):", minvalue=1, maxvalue=100)

        if hotkey and width and quality:
            profile_name = f"profile_{len(self.config['profiles'])+1}"
            self.config["profiles"][profile_name] = {"width": width, "quality": quality}
            self.config["hotkeys"][hotkey] = profile_name
            save_config(self.config)
            self.tree.insert("", tk.END, values=(hotkey, width, quality))

    def delete_entry(self):
        selected = self.tree.selection()
        if not selected:
            return
        for item in selected:
            hotkey = self.tree.item(item)["values"][0]
            profile = self.config["hotkeys"].pop(hotkey)
            self.config["profiles"].pop(profile, None)
            self.tree.delete(item)
        save_config(self.config)

def launch_gui():
    app = Configurator()
    app.mainloop()
