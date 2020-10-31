import cv2
import numpy as np

# https://www.youtube.com/watch?v=WQeoO7MI0Bs

img = cv2.imread("resources/Lena.png")
kernel = np.ones((5, 5), np.uint8)

# making an image gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray image", imgGray)

# making an image blur
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # kernel need to be odd numbers
# cv2.imshow("blur image", imgBlur)

# edge detection
imgCanny = cv2.Canny(img, 150, 200)
# cv2.imshow("canny", imgCanny)

# dialation
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# cv2.imshow("dialation", imgDialation)

# thinner image
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
# cv2.imshow("eroded", imgEroded)

cv2.waitKey(0)
