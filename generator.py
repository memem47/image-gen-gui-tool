from PIL import Image
import numpy as np

class ImageGenerator:
    def __init__(self, width=256, height=256, mode='RGB'):
        self.width = width
        self.height = height
        self.mode = mode

    def generate_random_image(self):
        if self.mode == 'RGB':
            array = np.random.randint(0, 256, (self.height, self.width, 3), dtype=np.uint8)
        elif self.mode == 'L':
            array = np.random.randint(0, 256, (self.height, self.width), dtype=np.uint8)
        else:
            raise ValueError("Unsupported mode. Use 'RGB' or 'L'.")
        return Image.fromarray(array, mode=self.mode)
    
    def save_image(self, image, path):
        image.save(path)