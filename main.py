import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import numpy as np
import cv2
import os

class ImageGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Generator")
        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.btn_generate = tk.Button(root, text="Generate Random Image", command=self.generate_image)
        self.btn_generate.pack()

        self.btn_save = tk.Button(root, text="Save Image", command=self.save_image)
        self.btn_save.pack()

        self.image = None

    def generate_image(self):
        array = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
        self.image = Image.fromarray(array)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_label.configure(image=self.tk_image)

    def save_image(self):
        if self.image is None:
            return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            self.image.save(path)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageGeneratorApp(root)
    root.mainloop()