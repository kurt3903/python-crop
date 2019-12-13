'''
This tool crops a 1 pixel border from each picture in the folder.
Ran successfully on May 10, 2019; do NOT run again unless you want to crop another 1 pixel border.
'''

from PIL import Image
import os
import random
import tkinter as tk
from tkinter import filedialog

def crop(image_path, coords, saved_location):

    """
    Parameters:

    image_path: The path to the image to edit
    coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()


#Prompt folder path:

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()

files = os.listdir(folder_path)
print(len(files))

if FileNotFoundError: quit()

for i in range(0, len(files)):

    print('Processing ' + files[i])

    image = folder_path + r"\\" + str(files[i])
    im = Image.open(image)

    width, height = im.size

    #Specify number of pixels to crop from border
    pixels = 1

    coords = (pixels, pixels, width - pixels, height - pixels)

    #crop the image
    crop(image, coords, image)
