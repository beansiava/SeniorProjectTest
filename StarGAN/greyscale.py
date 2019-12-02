from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def calculate(source, step):
    print('Calculating step' + str(step))
    n = Image.open(source)
    m = n.load()
    s = n.size
    for x in range(s[0]):
        for y in range(s[1]):

            r, g, b = m[x, y]
            final = (r + g + b)/3
            rVal = int((final - r)/(5.0 - step) + r)
            gVal = int((final - g)/(5.0 - step) + g)
            bVal = int((final - b)/(5.0 - step) + b)
            m[x, y] = rVal, gVal, bVal
    pre = source[:23]
    post = source[24:]
    n.save(pre + str(step+1) + post, "JPEG")


def split(source):
    im = Image.open(source)
    # crop_rectangle = (left, top, right, bottom)

    # Happy
    crop_rectangle = (640, 0, 768, 128)
    cropped_im = im.crop(crop_rectangle)
    cropped_im.save(source[:23] + "happy" + source[23] + ".jpg", "JPEG")

    # Neutral
    crop_rectangle = (768, 0, 896, 128)
    cropped_im = im.crop(crop_rectangle)
    cropped_im.save(source[:23] + "neutral" + source[23] + ".jpg", "JPEG")

    # Sad
    crop_rectangle = (896, 0, 1024, 128)
    cropped_im = im.crop(crop_rectangle)
    cropped_im.save(source[:23] + "sad" + source[23] + ".jpg", "JPEG")

    # Angry
    crop_rectangle = (128, 0, 256, 128)
    cropped_im = im.crop(crop_rectangle)
    cropped_im.save(source[:23] + "angry" + source[23] + ".jpg", "JPEG")
    return


if __name__ == '__main__':
    source = 'stargan_custom/results/1-images.jpg'
    for x in range(4):
        calculate(source, x+1)
    for x in range(5):
        split(source[:23] + str(x+1) + source[24:])
