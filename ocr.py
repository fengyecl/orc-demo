import pytesseract

from PIL import Image
import numpy as np

image = Image.open('test.png')

code = pytesseract.image_to_string(image, lang='eng')

print(code)
