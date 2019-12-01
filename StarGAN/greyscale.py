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

# Order: Angry, Contemptuous, Disgusted, Fearful, Happy, Neutral, Sad, Surprised


def split(source):
    im = Image.open("stargan_celeba_128/results/1-images.jpg")
    crop_rectangle = (0, 0, 128, 128)
    cropped_im = im.crop(crop_rectangle)
    for x in range():


source = 'stargan_custom/results/1-images.jpg'
for x in range(4):
    calculate(source, x+1)
for x in range(5):
    split(source[:23] + str(x+1) + source[24:])
