import cv2
from datetime import datetime

print("Practical 03 - Rotate Image")
print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# Read image made in Practical 01
img = cv2.imread("input_images/sample_image.png")

print("Original image shape:", img.shape)

height, width = img.shape[:2]
center = (width // 2, height // 2)

# Rotate image by 45 degrees
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imwrite("output_images/03_rotated_image.png", rotated)

print("Image rotated by 45 degrees")
print("Rotated image saved")
print("Output file: output_images/03_rotated_image.png")
