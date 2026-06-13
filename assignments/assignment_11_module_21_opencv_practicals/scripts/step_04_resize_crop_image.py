import cv2
from datetime import datetime
from pathlib import Path


print("OpenCV Practical 04: Resize and Crop Image")
print("------------------------------------------")
print("System timestamp:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

input_path = Path("input_images/sample_input_image.png")

resized_output_path = Path("output_images/step_04_resized_image.png")
cropped_output_path = Path("output_images/step_04_cropped_image.png")

image = cv2.imread(str(input_path))

if image is None:
    print("Error: Input image could not be read.")
    print("Please check whether this file exists:", input_path)
else:
    print("Original image read successfully.")
    print("Input image path:", input_path)
    print("Original image shape:", image.shape)
    print("Original image data type:", image.dtype)

    resized_image = cv2.resize(image, (300, 200))

    print("Image resized successfully.")
    print("Resized image shape:", resized_image.shape)

    cv2.imwrite(str(resized_output_path), resized_image)

    print("Resized image saved successfully.")
    print("Resized output path:", resized_output_path)

    cropped_image = image[80:320, 150:450]

    print("Image cropped successfully.")
    print("Cropped image shape:", cropped_image.shape)

    cv2.imwrite(str(cropped_output_path), cropped_image)

    print("Cropped image saved successfully.")
    print("Cropped output path:", cropped_output_path)
