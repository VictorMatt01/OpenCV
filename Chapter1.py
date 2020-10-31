import cv2
print("Package Imported")

# https://www.youtube.com/watch?v=WQeoO7MI0Bs

# -----------------------------------------------------------
# Learning how to import a picture
img = cv2.imread("resources/Lena.png")

# uncomment for it to work
# cv2.imshow("output", img)
# cv2.waitKey(0)
# -----------------------------------------------------------

# -----------------------------------------------------------
# Learning how to import a video
cap = cv2.VideoCapture("resources/test_video.mp4")

# change false to true to activate this part of the code
while False:
    # test if successful
    success, imgVideo = cap.read()
    cv2.imshow("Video", imgVideo)

    # add a delay and look for a key to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# -----------------------------------------------------------

cap_cam = cv2.VideoCapture(0)  # 0 for the standard camera
cap_cam.set(3, 640)
cap_cam.set(4, 480)
cap_cam.set(10, 100)  # adjust the clearity

while True:
    # test if successful
    success, imgVideo = cap_cam.read()
    cv2.imshow("Video", imgVideo)

    # add a delay and look for a key to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

