import cv2
import numpy as np

img = cv2.imread('p001.jpg', cv2.IMREAD_COLOR)
tmp = img[:, :]
height, width = img.shape[:2]
if (height > width):
    size = height
    limit = width
else:
    size = width
    limit = height
start = int((size - limit) / 2)
fin = int((size + limit) / 2)
# print(size)
new_img = cv2.resize(np.zeros((1, 1, 3), np.uint8), (size, size))

cv2.resize
if (size == height):
    new_img[:, start:fin] = tmp
    cv2.imwrite("test.jpg", new_img)
else:
    new_img[start:fin, :] = tmp
    cv2.imwrite("test.jpg", new_img)
