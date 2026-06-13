import cv2
from datetime import datetime

print("Practical 02 - Resize and Crop Image")
print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# Read the image created in Practical 01
img = cv2.imread("input_images/sample_image.png")

print("Original image shape:", img.shape)

# Resize the image
resized = cv2.resize(img, (240, 180))
cv2.imwrite("output_images/02_resized_image.png", resized)

print("Resized image saved")
print("Resized image shape:", resized.shape)

# Crop the image using row and column range
cropped = img[80:280, 120:360]
cv2.imwrite("output_images/02_cropped_image.png", cropped)

print("Cropped image saved")
print("Cropped image shape:", cropped.shape)
