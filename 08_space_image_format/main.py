"""
Soltution to Day 8 of the Advent of Code 2019.
Title: 'Space Image Format'
URL: https://adventofcode.com/2019/day/08
Author: tmpr
Date: 21th of February
"""

from space_image import SpaceImage

def main():
    with open("image_encoded.txt", "r") as f:
        image_input = f.read()
    my_image = SpaceImage(image_input)
    print("Pixels in densest layer: ", my_image.max_layer_count())
    my_image.visualize()

if __name__ == "__main__":
    main()
