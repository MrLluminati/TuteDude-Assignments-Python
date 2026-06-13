import cv2
import numpy as np
from datetime import datetime

print("OpenCV setup test successful.")
print("cv2 version:", cv2.__version__)
print("numpy version:", np.__version__)
print("System timestamp:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# Create a simple test image using NumPy
image = np.zeros((300, 500, 3), dtype=np.uint8)

# Draw simple shapes and text using OpenCV
cv2.rectangle(image, (50, 50), (450, 250), (255, 255, 255), 3)
cv2.circle(image, (250, 150), 60, (255, 255, 255), 2)
cv2.putText(
    image,
    "OpenCV Setup Test",
    (95, 285),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 255),
    2
)

output_path = "output_images/step_01_opencv_setup_test.png"
cv2.imwrite(output_path, image)

print("Test image created successfully.")
print("Output image saved at:", output_path)
