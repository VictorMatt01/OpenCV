import cv2

import numpy as np
# https://www.youtube.com/watch?v=WQeoO7MI0Bs

img = cv2.imread("resources/lambo.png")

print(img.shape)  # Height, width, rgb

# resizing an image
imgResize = cv2.resize(img, (300, 200))  # (width, height)

print(imgResize.shape)  # Height, width, rgb

# Cropping an image
imgCropped = img[0:200, 200:500]  # first height then width


cv2.imshow("lambo", img)
# cv2.imshow("lambo2", imgResize)
cv2.imshow("lamboCropped", imgCropped)

cv2.waitKey(0)

