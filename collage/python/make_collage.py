# -*- coding: utf-8 -*-
# script to blend a series of image in a 3x3 collage
# ref 28_11_2016 d90 folder, etude_de_la_bataille_contre_une_decadance_imminente.jpg
import os
from PIL import Image, ImageFilter


ROOT_FOLDER = "/Users/fruizdearcaute/Desktop/collage"
ORIG_FOLDER = os.path.join(ROOT_FOLDER, "orig")
PROC_FOLDER = os.path.join(ROOT_FOLDER, "proc")


def load_images(path):
    files = os.listdir(path)
    file_paths = [os.path.join(path, fil) for fil in files if os.path.splitext(fil)[1] == ".JPG"]
    file_paths.sort()
    images = []

    for fil in file_paths:
        img = Image.open(fil)
        img = img.point(lambda p: p * 1.4) #brighten the image
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
    new_size = (images[0].size[0]*int(len(images)/3), images[0].size[1]*int(len(images)/3))
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
    frame.save(os.path.join(PROC_FOLDER, "etude_de_la_bataille_contre_une_decadance_imminente.JPG"), "JPEG")
