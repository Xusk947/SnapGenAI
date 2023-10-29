import requests
import numpy as np
import cv2
import imutils
import tkinter as tk

from PIL import ImageTk, Image

class Camera:
    """
    Represents a camera connected to a phone.
    """

    def __init__(self, url):
        self.url = url

    def get_capture(self):
        """
        Fetches a video frame from the phone's camera and displays it.
        """
        # Fetch the image from the URL
        img_resp = requests.get(self.url)
        # Convert the image content to a numpy array
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)

        # Decode the image array into an image
        img = cv2.imdecode(img_arr, -1)

        # Resize the image to a specific width and height
        img = imutils.resize(img, width=1000, height=1800)

        return img

    def get_capture_for_tkinter(self):
        capture = self.get_capture()

        imgtk = ImageTk.PhotoImage(image=Image.fromarray(capture))

        return imgtk

