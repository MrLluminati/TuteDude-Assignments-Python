import cv2
import numpy as np
from datetime import datetime

print("Practical 05 - Affine Transformation")
print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# Read the image from Practical 01
img = cv2.imread("input_images/sample_image.png")

print("Original image shape:", img.shape)

rows, cols = img.shape[:2]

# Three points from the original image
pts1 = np.float32([
    [60, 60],
    [420, 60],
    [60, 300]
])

# New positions of those three points
pts2 = np.float32([
    [40, 90],
    [400, 40],
    [100, 320]
])

matrix = cv2.getAffineTransform(pts1, pts2)

affine_img = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imwrite("output_images/05_affine_transform.png", affine_img)

print("Affine transformation applied")
print("Output image saved")
print("Output file: output_images/05_affine_transform.png")
