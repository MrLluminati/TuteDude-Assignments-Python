import cv2
from datetime import datetime

print("Practical 04 - Threshold Image")
print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# Read the image from Practical 01
img = cv2.imread("input_images/sample_image.png")

print("Original image shape:", img.shape)

# Convert image to grayscale first
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output_images/04_gray_image.png", gray)

print("Gray image saved")

# Apply simple binary threshold
ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

cv2.imwrite("output_images/04_threshold_image.png", thresh)

print("Threshold value used:", ret)
print("Threshold image saved")
print("Output file: output_images/04_threshold_image.png")
