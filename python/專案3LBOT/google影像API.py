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
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\ASUS\Downloads\My First Project-e33222a7ad3c.json"
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
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\ASUS\Downloads\My First Project-e33222a7ad3c.json"
# Instantiates a client
client = vision.ImageAnnotatorClient()


response = client.annotate_image({'image': {'source': {'image_uri': 'https://00e9e64bac369eb881717e0d768d21d8174c2db20aa97136ae-apidata.googleusercontent.com/download/storage/v1/b/mona01/o/LinusTorvalds.jpg?qk=AD5uMEuV3bdIvISa___f3NgCiBqYbWPEn3-2mOmJhVMK-z088a1uBzmo9BvRAQREHCOkTCfOeCbToDycq-EQXrYsxmfcehn_9vOTWw1pcMeQ1hXnYmwPw-u0UUn-1aaVkhqpn2AnHmjUaavyj5GnHYcxKVqtRa7PuS17c2uVLO6put77z_cZuAvXN-_sZ0UeeKO8igRu2fraSzuJ8cKerYIko_3aCd-gWh2IuBjVWksdBjZZTTN8qXECbUs6CMrSfss6lFA65EywltoYswqxz3ph60xULfZAK5n1u1KkE6KDr5JlRkj_6jgnG1rIsu8yYLkfPrkx4wc92kF3BUYjJWunBu4xdOpJ25tBRfOFd-8t84SRniDfRrVJJdwGTSQll7tEQ0hn3c9BxW50XcLq7uR3Z2rcN4dArHPAgVm3gvQ-TfCMZWTglaegraYBgTfzycvmlf9ijSS09MJ5FkZxuWwFQ5movgMyydzWKGxyxx1RtMOStR56oRHaqBZYT1Z1PaZiVHyPiXYAcZAnAWjhy9bsJOqgZ9KQW_eKtD2C2KxS2f69S-SRYhqth24_TNV1F4LokYBC30Cx6LLo7veV7p5qM2LFsgXHNmuMOIu2DhMkBLnSwKc9W0cGmwxczdj77iEFb6XH-FA20K4lcCkU9BUnMeyVDlioFgHdsGib5JCqYr9X1DltR3pK9gbJB5k79dscHBWJnh3L6h597nxgMD6XpLbq-in1OWw8X84k5k9kAek6RbZRBydCQw1gbLdggwjXrCFf7dPWLU2RctO4Ws5h2ywRfHFx7eq7PXxtUcFZlPfgVPwifcM&isca=1'}}, 'features': [{'type': vision.enums.Feature.Type.LABEL_DETECTION}],})

print(response)