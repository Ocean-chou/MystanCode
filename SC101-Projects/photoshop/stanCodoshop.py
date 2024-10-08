"""
File: stanCodoshop.py
Name: Ocean
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    red_dist = red - pixel.red
    green_dist = green - pixel.green
    blue_dist = blue - pixel.blue
    color_dist = (red_dist**2 + green_dist**2 + blue_dist**2)**0.5
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    rgb = []
    red_sum = 0
    green_sum = 0
    blue_sum = 0
    count = 0
    for pixel in pixels:
        red_sum += pixel.red
        green_sum += pixel.green
        blue_sum += pixel.blue
        count += 1
    rgb.append(red_sum//count)
    rgb.append(green_sum//count)
    rgb.append(blue_sum//count)
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    rgb_average = get_average(pixels)
    closest_color_dist = 0
    best_pixel = pixels[0]
    for pixel in pixels:
        color_dist = get_pixel_dist(pixel, rgb_average[0], rgb_average[1], rgb_average[2])
        # Set the first pixel as the reference point.
        if pixel == pixels[0]:
            closest_color_dist = color_dist
        # The other pixel compare with the first pixel.
        else:
            if color_dist < closest_color_dist:
                closest_color_dist = color_dist
                best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            result_p = result.get_pixel(x, y)
            pixels = []
            for image in images:
                img_pixel = image.get_pixel(x, y)
                pixels.append(img_pixel)        # Store the same pixel from each image into the list.
            result_p.red = get_best_pixel(pixels).red
            result_p.green = get_best_pixel(pixels).green
            result_p.blue = get_best_pixel(pixels).blue
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
