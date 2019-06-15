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

import cv2
import os

imgpath = r"D:\DCIM\100ND40X"

for filename in os.listdir(imgpath):
    path = os.path.join(imgpath,filename)
    img = cv2.imread(path)
    print(img)
    height, width, channels = img.shape

    height_split = 1
    width_split = 2
    new_img_height = int(height / height_split)
    new_img_width = int(width / width_split)

    for h in range(height_split):
        height_start = h * new_img_height
        height_end = height_start + new_img_height

        for w in range(width_split):
            width_start = w * new_img_width
            width_end = width_start + new_img_width
            if not os.path.isdir(imgpath + "_1"):
                os.makedirs(imgpath + "_1")
            file_name = imgpath + "_1\\" + filename.split(".")[0] + "_" + str(h) + "_" + str(w) + ".jpg"
            print(file_name)
            clp = img[height_start:height_end, width_start:width_end]
            cv2.imwrite(file_name, clp)

