import cv2
from datetime import datetime
from pathlib import Path


print("OpenCV Practical 03: Convert Image to Grayscale")
print("-----------------------------------------------")
print("System timestamp:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

input_path = Path("input_images/sample_input_image.png")
output_path = Path("output_images/step_03_grayscale_image.png")

image = cv2.imread(str(input_path))

if image is None:
    print("Error: Input image could not be read.")
    print("Please check whether this file exists:", input_path)
else:
    print("Original image read successfully.")
    print("Input image path:", input_path)
    print("Original image shape:", image.shape)
    print("Original image data type:", image.dtype)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    print("Image converted to grayscale successfully.")
    print("Grayscale image shape:", grayscale_image.shape)
    print("Grayscale image data type:", grayscale_image.dtype)

    cv2.imwrite(str(output_path), grayscale_image)

    print("Grayscale image saved successfully.")
    print("Output image path:", output_path)
