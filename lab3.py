
import cv2
import numpy as np

img = cv2.imread("IMAGE.jpg")

if img is None:
    print("Image not found!")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([
        [0, 0],
        [cols-1, 0],
        [0, rows-1]
    ])

    pts2 = np.float32([
        [50, 50],
        [cols-50, 100],
        [100, rows-50]
    ])

    matrix = cv2.getAffineTransform(pts1, pts2)

    print("Transformation Matrix:")
    print(matrix)

    result = cv2.warpAffine(img, matrix, (cols, rows))

    cv2.imshow("Original Image", img)
    cv2.imshow("Affine Transformation", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
