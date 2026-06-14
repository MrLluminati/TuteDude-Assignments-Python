import cv2
import numpy as np
from datetime import datetime
from pathlib import Path

print("Practical 06 - Video Processing")
print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

input_video = Path("input_videos/sample_video.avi")
output_video = Path("output_videos/06_processed_video.avi")
sample_frame = Path("output_images/06_sample_processed_frame.png")

width = 480
height = 360
fps = 10

# First I am creating a small sample video
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
writer = cv2.VideoWriter(str(input_video), fourcc, fps, (width, height))

for i in range(30):
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    x = 40 + (i * 10)
    cv2.rectangle(frame, (60, 80), (420, 300), (255, 255, 255), 2)
    cv2.circle(frame, (x, 180), 35, (255, 255, 255), 2)
    cv2.putText(frame, "Sample Video", (140, 335), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    writer.write(frame)

writer.release()
print("Sample video created:", input_video)

# Now I am reading the video using cv2.VideoCapture
cap = cv2.VideoCapture(str(input_video))

print("Video opened:", cap.isOpened())

frame_count = 0

out = cv2.VideoWriter(str(output_video), fourcc, fps, (width, height), isColor=False)

while True:
    ret, frame = cap.read()

    if ret == False:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray)

    if frame_count == 5:
        cv2.imwrite(str(sample_frame), gray)

    frame_count = frame_count + 1

cap.release()
out.release()

print("Total frames processed:", frame_count)
print("Processed video saved:", output_video)
print("Sample processed frame saved:", sample_frame)
