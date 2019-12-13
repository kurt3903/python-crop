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
    #cropped_image.show()


#Prompt folder path:

root = tk.Tk()
root.withdraw()

try:
    folder_path = filedialog.askdirectory()

    files = os.listdir(folder_path)
    # Specify number of pixels to crop from border
    pixels = int(input('Number of pixels to crop: '))
    for i in files:
        print('Processing ' + i)

        image = folder_path + r"\\" + str(i)
        im = Image.open(image)

        width, height = im.size

        coords = (pixels, pixels, width - pixels, height - pixels)

        #crop the image
        crop(image, coords, image)
except FileNotFoundError:
    print('No folder selected.')
    quit()
finally:
    print('\n Finished.')
