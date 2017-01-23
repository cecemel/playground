# -*- coding: utf-8 -*-
# script to blend a series of image in a 2x3 collage
# ref 15_12_2016 d90 folder, m.jpg
import os
from PIL import Image, ImageFilter, ImageEnhance


ROOT_FOLDER = "/Users/felix/Desktop/collage4"
ORIG_FOLDER = os.path.join(ROOT_FOLDER, "orig")
PROC_FOLDER = os.path.join(ROOT_FOLDER, "proc")


def load_images(path):
    files = os.listdir(path)
    file_paths = [os.path.join(path, fil) for fil in files if os.path.splitext(fil)[1] == ".JPG"]
    file_paths.sort()
    images = []

    for fil in file_paths:
        img = Image.open(fil)
        img = img.point(lambda p: p * 1.0)  # brighten the image
        contrast = ImageEnhance.Contrast(img)
        img = contrast.enhance(1.3) #improve contrast
        images.append(img)

    return images

def resize_image(image):
    # keep aspect ratio
    new_width = 384
    new_height = int(new_width * image.height / image.width)
    print(new_height)
    return image.resize((new_width, new_height), Image.ANTIALIAS)

def set_margin_image(image):
    """
    suppose image

    ***                              iiiii
    ***   current impl transforms to iiiii
    ***                              ii***
                                     ii***
                                     ii***


    :param image:
    :return:
    """
    new_size = (400, 270)
    new_im = Image.new("RGB", new_size, (255,255,255))
    new_im.paste(image, ((new_size[0] - image.size[0]), (new_size[1] - image.size[1])))
    return new_im

def fill_frame(images):
    """
    creates 3 by N grid needs refactor
    :param images:
    :return:
    """
    new_size = (images[0].size[0]*int(len(images)/2), images[0].size[1]*int(len(images)/3))
    new_im = Image.new("RGB", new_size, (255,255,255))

    #paste subsequent image
    col_height = 0
    col_number = 0
    row_height = 0
    row_number = 0

    for index in range(0, len(images)):
        col_height = col_number * images[0].size[0]

        new_im.paste(images[index], (col_height, row_height))

        col_number += 1

        if index > 0 and (index + 1) % 3 == 0:
            col_number = 0
            row_number += 1
            row_height = row_number * images[0].size[1]

    return new_im


def post_decorate_frame(frame):
    new_size = (frame.size[0] + 16, frame.size[1] + 15)
    new_im = Image.new("RGB", new_size, (255,255,255))
    new_im.paste(frame, (0,0))

    return new_im


def black_top_and_bottom_border(frame):
    new_size = (frame.size[0], frame.size[1] + 213)
    new_im = Image.new("RGB", new_size, (0, 0, 0))

    top_border = Image.new("RGB", (frame.size[0], 107), (0, 0, 0))
    new_im.paste(top_border, (0, 0))
    new_im.paste(frame, (0, top_border.size[1]))

    bottom_border = Image.new("RGB", (frame.size[0], 105), (0, 0, 0))

    new_im.paste(bottom_border, (0, top_border.size[1] + frame.size[1]))

    new_im.show()

    return new_im


if __name__ == "__main__":
    images = load_images(ORIG_FOLDER)
    mod_ims = []
    for i in images:
        mod_i = resize_image(i)
        mod_i = set_margin_image(mod_i)
        mod_ims.append(mod_i)

    frame = fill_frame(mod_ims)
    frame = post_decorate_frame(frame)
    frame = black_top_and_bottom_border(frame)

    print(frame.size[0], frame.size[1])
    frame.save(os.path.join(PROC_FOLDER, "test.JPG"),
               format='JPEG', subsampling=0, quality=100)
