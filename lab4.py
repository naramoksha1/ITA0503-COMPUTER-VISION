
import cv2
import numpy as np

img = cv2.imread("IMAGE.jpg")

if img is None:
    print("Image not found!")
else:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original Image", img)
    cv2.imshow("Binary Mask", mask)
    cv2.imshow("Extracted Object", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
