import cv2
from PIL import Image
import numpy as np
import random
import string
import os
from datetime import datetime

class ImageGenerator:
    def __init__(self, width=256, height=256, mode='RGB'):
        self.width = width
        self.height = height
        self.mode = mode

    def generate_random_image(self):
        canvas = np.ones((self.height, self.width, 3), dtype=np.uint8) * 255

        try:
            # random circle, square, and line
            for _ in range(random.randint(3, 10)):
                color = tuple(np.random.randint(0, 256, size=3).tolist())
                center = tuple(np.random.randint(0, min(self.width, self.height), size=2))
                radius = np.random.randint(self.width // 20, self.width // 5)
                cv2.circle(canvas, center, radius, color, -1)

                color = tuple(np.random.randint(0, 256, size=3).tolist())
                pt1 = tuple(np.random.randint(0, self.width, size=2))
                pt2 = tuple(np.random.randint(0, self.width, size=2))
                cv2.rectangle(canvas, pt1, pt2, color, -1)

                color = tuple(np.random.randint(0, 256, size=3).tolist())
                pt1 = tuple(np.random.randint(0, self.width, size=2))
                pt2 = tuple(np.random.randint(0, self.width, size=2))
                cv2.line(canvas, pt1, pt2, color, random.randint(1, 5))

            # random text
            for _ in range(random.randint(1, 30)):
                color = tuple(np.random.randint(0, 256, size=3).tolist())
                font = random.choice([cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_PLAIN])
                text = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))
                pt = tuple(np.random.randint(0, min(self.width, self.height), size=2))
                font_scale = random.uniform(0.5, 2)
                thickness = random.randint(1, 5)
                cv2.putText(canvas, text, pt, font, font_scale, color, thickness)

            # random noise
            noise = np.random.randint(0, 256, (self.height, self.width, 3), dtype=np.uint8)
            noise = cv2.GaussianBlur(noise, (random.randint(1, 5) * 2 + 1, random.randint(1, 5) * 2 + 1), 0)
            canvas = cv2.addWeighted(canvas, random.uniform(0.5, 1), noise, random.uniform(0.1, 0.5), 0)

            # random warp
            if random.random() < 0.5:
                pts1 = np.float32([[0, 0], [self.width-1, 0], [0, self.height-1], [self.width-1, self.height-1]])
                shift = np.random.randint(-self.width // 10, self.width // 10, size=(4, 2))
                pts2 = pts1 + shift
                pts2 = np.float32(pts2)
                M = cv2.getPerspectiveTransform(pts1, pts2)
                canvas = cv2.warpPerspective(canvas, M, (self.width, self.height))       

            # Convert to grayscale if needed
            if self.mode == 'L':
                canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
                
            return Image.fromarray(canvas)
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
    
    def save_image(self, image, path=None):
        if path is None:
            os.makedirs('output', exist_ok=True)
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = os.path.join('output', f"image_{now}.png")
        image.save(path)