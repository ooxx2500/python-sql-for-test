# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:12:26 2020

@author: ASUS
"""


import pytesseract
from PIL import Image

image= Image.open(r'C:\Users\ASUS\Downloads\20200727_07.jpg')
code=pytesseract.image_to_string(image)
print(code)