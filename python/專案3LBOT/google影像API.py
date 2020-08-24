# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:58:50 2020

@author: ASUS
"""


import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
# Importantance:set your json file in this part, I try to follow official guide but it didn't work, use below instead.T
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"‪C:\Users\莫再提\Desktop\GOOGLEKEY.json.json"
# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath(r'C:\Users\ASUS\Downloads\trump.jpg_1140x855.jpg_1140x855.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)


-------------------------------------------

import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
# Importantance:set your json file in this part, I try to follow official guide but it didn't work, use below instead.T
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\莫再提\Desktop\GOOG.json"
# Instantiates a client
client = vision.ImageAnnotatorClient()


response = client.annotate_image({'image': {'source': {'image_uri': 'gs://mona01/LinusTorvalds.jpg'}}, 'features': [{'type': vision.enums.Feature.Type.LABEL_DETECTION}],})

print(response)


---------------------------------------------



# Instantiates a client
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\莫再提\Desktop\GOOG.json"
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


path=r'C:\Users\莫再提\Downloads\01.jpg'
detect_text(path)

---------------------------------------------------------------

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    from google.cloud import vision
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\莫再提\Desktop\GOOG.json"
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
 

    for text in texts:   #印出塗上每個單字位置
        print('\n"{}"'.format(text.description))

    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                 for vertex in text.bounding_poly.vertices])

    #     print('bounds: {}'.format(','.join(vertices))) #印出塗上每個單字位置

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

uri=r'https://diz36nn4q02zr.cloudfront.net/webapi/images/r/SalePageDesc/2492625/image1.jpg'

detect_text_uri(uri)













