# Assignment 11: Module 21 - OpenCV Practicals

This project contains beginner-level OpenCV practical implementations for Assignment 11, Module 21.

The work is organised with scripts, generated output images, and screenshot proofs showing code, terminal output, output files, and system timestamp where applicable.

## Folder structure

```text
assignment_11_module_21_opencv_practicals/
├── README.md
├── input_images/
│   └── sample_input_image.png
├── output_images/
│   ├── step_01_opencv_setup_test.png
│   └── step_02_read_image_output.png
├── requirements.txt
├── screenshot_proofs/
│   ├── step_01_project_setup/
│   └── step_02_read_image/
└── scripts/
    ├── step_01_test_opencv_setup.py
    └── step_02_read_image.py
```

## Requirements

Install dependencies:

```powershell
pip install -r requirements.txt
```

Dependencies used:

```text
opencv-python
numpy
```

## Step 01 - OpenCV setup test

Script:

```text
scripts/step_01_test_opencv_setup.py
```

Purpose:

- import OpenCV and NumPy;
- print package versions;
- print system timestamp;
- create a blank image using NumPy;
- draw a rectangle, circle, and text using OpenCV;
- save the generated output image.

Output image:

```text
output_images/step_01_opencv_setup_test.png
```

Screenshot proofs:

```text
screenshot_proofs/step_01_project_setup/
```

## Step 02 - Read and save image

Script:

```text
scripts/step_02_read_image.py
```

Purpose:

- create a sample input image if it is not already available;
- read the image using cv2.imread();
- print the image path, shape, and data type;
- save the read image using cv2.imwrite();
- confirm the generated output image.

Input image:

```text
input_images/sample_input_image.png
```

Output image:

```text
output_images/step_02_read_image_output.png
```

Screenshot proofs:

```text
screenshot_proofs/step_02_read_image/
```

## Progress checklist

- [x] Step 01: Project folder structure created
- [x] Step 01: Requirements file added
- [x] Step 01: OpenCV and NumPy installed
- [x] Step 01: Setup test script created
- [x] Step 01: Output image generated
- [x] Step 01: Screenshot proofs added
- [x] Step 02: Image reading script created
- [x] Step 02: Input image generated
- [x] Step 02: Image read using OpenCV
- [x] Step 02: Output image saved
- [x] Step 02: Screenshot proofs added
- [ ] Step 03: Grayscale image practical
- [ ] Step 04: Resize/crop practical
- [ ] Step 05: Drawing practical
- [ ] Step 06: Final testing and ZIP submission
