import cv2
from datetime import datetime
from pathlib import Path

print("Practical 07 - Webcam Capture")
print("Time:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

output_folder = Path("output_images")
output_folder.mkdir(exist_ok=True)

working_camera_found = False

# Trying a few camera indexes because sometimes index 0 is a virtual camera
for camera_index in range(4):
    print("Trying camera index:", camera_index)

    camera = cv2.VideoCapture(camera_index)

    print("Camera opened:", camera.isOpened())

    if camera.isOpened():
        frame = None
        ret = False

        # Read a few frames so camera can adjust
        for i in range(20):
            ret, frame = camera.read()

        if ret:
            output_path = output_folder / f"07_webcam_capture_index_{camera_index}.png"
            cv2.imwrite(str(output_path), frame)

            print("Frame captured successfully from camera index:", camera_index)
            print("Captured frame shape:", frame.shape)
            print("Output file:", output_path)

            working_camera_found = True
        else:
            print("Frame could not be captured from camera index:", camera_index)

        camera.release()
    else:
        print("Camera index not available:", camera_index)

print("Webcam/camera capture test completed.")

if working_camera_found:
    print("At least one camera source was captured successfully.")
else:
    print("No webcam/camera source could be captured.")
    print("Please check camera permission or connect a webcam.")
