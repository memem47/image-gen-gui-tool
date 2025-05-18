import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk
from generator import ImageGenerator
import datetime

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Generator")
            
        self.generator = ImageGenerator()
        self.image = None

        self.mode_var = tk.StringVar(value='RGB')
        tk.Label(root, text="Image Mode").pack()
        ttk.Combobox(root, textvariable=self.mode_var, values=["RGB", "L"]).pack()

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.btn_generate = tk.Button(root, text="Generate Random Image", command=self.generate_image)
        self.btn_generate.pack()

        self.btn_save = tk.Button(root, text="Save Image", command=self.save_image)
        self.btn_save.pack()

    def generate_image(self):
        self.generator.mode = self.mode_var.get()
        self.image = self.generator.generate_random_image()
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_label.configure(image=self.tk_image)
        
    def save_image(self):
        if self.image is None:
            return
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        default_filename = f"image_{now}.png"

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            initialfile=default_filename,
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if path:
            self.generator.save_image(self.image, path)