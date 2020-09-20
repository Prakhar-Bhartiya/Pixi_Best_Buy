from __future__ import print_function
import pyrebase
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
from skimage import io


config = {
    "apiKey": "AIzaSyD9wBi2DimEgStis9xabFlw9TW47-DcrFc",
    "authDomain": "bestbuy-2c3c8.firebaseapp.com",
    "databaseURL": "https://bestbuy-2c3c8.firebaseio.com",
    "projectId": "bestbuy-2c3c8",
    "storageBucket": "bestbuy-2c3c8.appspot.com",
    "messagingSenderId": "118330007537",
    "appId": "1:118330007537:web:1a436ff3a89cdf3c126e50",
    "measurementId": "G-NMFBC77LTS"
}
def decode(im) :
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  # Print results
  barcode = list()
  for obj in decodedObjects:
    barcode.append(obj.data)

  return barcode

def main():
    firebase  = pyrebase.initialize_app(config)
#storage = firebase.storage()

    path_on_cloud = "images/test.jpg"

    path_local = "202.jpg"

    db = firebase.database()
    storage = firebase.storage()

    imgurl=storage.child(path_on_cloud).put(path_local)
    img_url=storage.child(path_on_cloud).get_url(imgurl['downloadTokens'])

#print(img_url)

#storage.child(path_on_cloud).put(path_local)

#image_url = storage.child(path_on_cloud).get_url(config)
#image_url = ""
#print(image_url+"\n")

    temp = decode(io.imread(img_url))

    return temp
