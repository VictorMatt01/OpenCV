import cv2

import numpy as np

img = cv2.imread('resources/Lena.png')

horImg = np.hstack((img, img))

verImg = np.vstack((img, img))

cv2.imshow("stack", horImg)

cv2.imshow("stack ver", verImg)

cv2.waitKey(0)
