import cv2
import numpy as np
from datetime import datetime
from pathlib import Path


print("OpenCV Practical 05: Draw Shapes and Text")
print("----------------------------------------")
print("System timestamp:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

output_path = Path("output_images/step_05_draw_shapes_text.png")

image = np.zeros((500, 700, 3), dtype=np.uint8)

cv2.line(image, (50, 50), (650, 50), (255, 255, 255), 3)
cv2.rectangle(image, (50, 100), (300, 250), (255, 255, 255), 3)
cv2.circle(image, (500, 175), 80, (255, 255, 255), 3)
cv2.putText(
    image,
    "OpenCV Drawing Practical",
    (120, 350),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)
cv2.putText(
    image,
    "Line | Rectangle | Circle | Text",
    (130, 410),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 255, 255),
    2
)

cv2.imwrite(str(output_path), image)

print("Blank image created successfully.")
print("Line drawn successfully.")
print("Rectangle drawn successfully.")
print("Circle drawn successfully.")
print("Text written successfully.")
print("Output image saved at:", output_path)
