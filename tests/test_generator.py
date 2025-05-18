import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generator import ImageGenerator
import numpy as np

def test_image_generation():
    gen = ImageGenerator()
    image = gen.generate_random_image()
    assert image.size ==(256, 256)
    assert image.mode == 'RGB'

def test_grayscale_image_generation():
    gen = ImageGenerator(mode='L')
    image = gen.generate_random_image()
    assert image.size == (256, 256)
    assert image.mode == 'L'

def test_image_save(tmp_path):
    gen = ImageGenerator()
    image = gen.generate_random_image()
    save_path = tmp_path / "test_image.png"
    gen.save_image(image, save_path)
    assert os.path.exists(save_path)