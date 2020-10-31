import cv2
import numpy as np

# https://www.youtube.com/watch?v=WQeoO7MI0Bs
# this chapter explains how to draw or write on an image

# make a black image, all black values = 0
img = np.zeros((512, 512, 3), np.uint8)

# making a part blue
# img[200:300, 100:300, :] = 255, 0, 0

# drawing a green line across the black image
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# draw a rectangle
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

# fill a rectangle
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)

# drawing a circle
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

# putting text on an image
cv2.putText(img, "OPENCV", (300, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

cv2.imshow("black", img)

cv2.waitKey(0)

