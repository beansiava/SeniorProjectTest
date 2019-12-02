import argparse
import os
from PIL import Image


def main(config):

    if config.mode == 'pre':
        print('Resizing input image')
        for filename in os.listdir("data/RaFD/test/angry/"):
            dst = "000001.jpg"
            src = 'data/RaFD/test/angry/' + filename
            dst = 'data/RaFD/test/angry/' + dst

            # rename() function will
            # rename all the files
            os.rename(src, dst)

        # Resize the picture
        # basewidth = 256
        basewidth = 128
        img = Image.open('data/RaFD/test/angry/000001.jpg')
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save('data/RaFD/test/angry/000001.jpg')

    elif config.mode == 'post1':
        im = Image.open("stargan_celeba_128/results/1-images.jpg")
        crop_rectangle = (128, 0, 256, 128)
        cropped_im = im.crop(crop_rectangle)
        cropped_im.show()

    else:
        im = Image.open("stargan_celeba_128/results/1-images.jpg")
        crop_rectangle = (256, 0, 384, 128)
        cropped_im = im.crop(crop_rectangle)
        cropped_im.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Training configuration.
    parser.add_argument('--mode', type=str,
                        default='pre', choices=['pre', 'post1', 'post2'])

    config = parser.parse_args()
    print(config)
    main(config)
