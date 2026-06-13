import cv2
import numpy as np
from datetime import datetime
from pathlib import Path


print("OpenCV Practical 02: Read and Save Image")
print("----------------------------------------")
print("System timestamp:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

input_folder = Path("input_images")
output_folder = Path("output_images")

input_folder.mkdir(exist_ok=True)
output_folder.mkdir(exist_ok=True)

input_path = input_folder / "sample_input_image.png"
output_path = output_folder / "step_02_read_image_output.png"

# Create a sample input image if it does not already exist
if not input_path.exists():
    sample_image = np.zeros((400, 600, 3), dtype=np.uint8)

    cv2.rectangle(sample_image, (50, 50), (550, 350), (255, 255, 255), 3)
    cv2.circle(sample_image, (300, 200), 80, (255, 255, 255), 3)
    cv2.putText(
        sample_image,
        "Sample Input Image",
        (145, 380),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imwrite(str(input_path), sample_image)
    print("Sample input image created at:", input_path)

# Read the image using OpenCV
image = cv2.imread(str(input_path))

if image is None:
    print("Error: Image could not be read.")
else:
    print("Image read successfully.")
    print("Input image path:", input_path)
    print("Image shape:", image.shape)
    print("Image data type:", image.dtype)

    cv2.imwrite(str(output_path), image)

    print("Image saved successfully.")
    print("Output image path:", output_path)
