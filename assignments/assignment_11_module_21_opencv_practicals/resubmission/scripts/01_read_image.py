import cv2
import numpy as np
from datetime import datetime

print("Practical 01 - Read Image")
print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# I am first making a simple sample image
img = np.zeros((360, 480, 3), dtype=np.uint8)

cv2.rectangle(img, (60, 60), (420, 300), (255, 255, 255), 2)
cv2.circle(img, (240, 180), 70, (255, 255, 255), 2)
cv2.putText(img, "Sample Image", (135, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

cv2.imwrite("input_images/sample_image.png", img)
print("Sample image saved in input_images folder")

# Now I am reading the image using OpenCV
read_img = cv2.imread("input_images/sample_image.png")

print("Image read using cv2.imread")
print("Image shape:", read_img.shape)

cv2.imwrite("output_images/01_read_image_output.png", read_img)
print("Read image saved in output_images folder")
