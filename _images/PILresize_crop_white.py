# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from PIL import Image
import os

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

imgpath = r"D:\new"

for filename in os.listdir(imgpath):
    path = os.path.join(imgpath,filename)
    im = Image.open(path)
    new_file_name = imgpath + "_3\\" + filename.split(".")[0] + "_1.jpg"
    if not os.path.isdir(imgpath + "_3"):
        os.makedirs(imgpath + "_3")
    print(path)
    im_new = add_margin(im, 300, 300, 300, 300, (255, 255, 255))
    im_new.save(new_file_name, quality=100)

