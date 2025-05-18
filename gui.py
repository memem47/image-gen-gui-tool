import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
from generator import ImageGenerator

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Generator")

        self.generator = ImageGenerator()
        self.image = None

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.btn_generate = tk.Button(root, text="Generate Random Image", command=self.generate_image)
        self.btn_generate.pack()

        self.btn_save = tk.Button(root, text="Save Image", command=self.save_image)
        self.btn_save.pack()

    def generate_image(self):
        self.image = self.generator.generate_random_image()
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_label.configure(image=self.tk_image)
        
    def save_image(self):
        if self.image is None:
            return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            self.generator.save_image(self.image, path)