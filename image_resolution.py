#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from PIL import Image

# decoration
print(stylize("\n---- | Get the resolution of an image | ----\n", fg("red")))

# user interaction
image_name = input("Image name: ")

# function
def get_resolution_of(img):
    image = Image.open(img)
    width, height = image.size
    return width, height

# output
width, height = get_resolution_of(image_name)
print(f"\nWidth of the image: {width} px\nHeigth of the image: {height} px\n")
