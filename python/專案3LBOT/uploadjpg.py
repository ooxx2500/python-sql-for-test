# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:04:22 2020

@author: 莫再提
"""


import numpy as np
import matplotlib.pyplot as plt
import pyimgur

def glucose_graph():
    """
    plt.figure(figsize=(240,240))
    plt.plot(ug)
    plt.savefig('send.png')
    """
    # normal_samples = np.random.normal(size = 100000)
    # uniform_samples = np.random.uniform(size = 100000)
    # plt.hist(normal_samples)
    # plt.savefig('send.png')
    CLIENT_ID = "ooxx2500@gmail.com"
    PATH = r"C:\Users\莫再提\Desktop\0001.jpg"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")
    return uploaded_image.link
img_url = glucose_graph()
print(img_url)


