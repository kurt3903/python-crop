'''
This tool crops a 1 pixel border from each picture in the folder.
Ran successfully on May 10, 2019; do NOT run again unless you want to crop another 1 pixel border.
'''

from PIL import Image
import os
import random

def crop(image_path, coords, saved_location):

    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    #cropped_image.show()

path = r""
files = os.listdir(path)

for i in range(0, len(files) + 1):

    print(files[i])

    image = path+ r"\\" + str(files[i])
    im = Image.open(image)

    width, height = im.size

    coords = (1,1, width, height)
    #im.show()

    #crop the image
    crop(image, (1, 1, width - 1, height - 1), image)