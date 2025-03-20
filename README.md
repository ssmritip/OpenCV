
# Learning OpenCV

This repository is for exploring and learning the fundamentals of OpenCV. It includes various tasks aimed at understanding basic image processing, creating a virtual painter using hand gestures, and implementing simple face detection.

## Project Structure

```
├── Assets/              # Resources used in the projects
├── Basics/              # Basic OpenCV operations
│   ├── read.py          # Read images and videos
│   ├── rescale.py       # Image rescaling operations
│   └── draw.py          # Basic usage of OpenCV draw functions
├── Project_Virtual_Painter/     # Virtual Painter using MediaPipe
│   └── canvas.py       
│   └── drawing.py   
│   └── main.py   
├── README.md
└── face_detection/      # Simple face detection using face_detection.ipynb 
```

## Basics

### 1. `read.py`
This file demonstrates how to read images and videos using OpenCV.

### 2. `rescale.py`
Shows how to rescale images to different sizes.

### 3. `draw.py`
Illustrates the basic drawing functions available in OpenCV (like `cv2.line`, `cv2.circle`, etc.).

## Virtual Painter

In the `Project_Virtual_Painter` folder, a virtual painting application is created using hand gestures. MediaPipe is used for detecting hand landmarks, and drawing on the screen is controlled by finger movements..

### Key Features:
- **Drawing**: When the index finger is raised, drawing is activated on the screen.
- **Color Change**: A combination of index and middle fingers raised will change the drawing color.
- **Reset Canvas**: The thumb raised for 20 consecutive frames clears the canvas.

## Face Detection

In this folder, a simple face detection script using OpenCV's Haar Cascade Classifier is implemented.

### Steps:
1. Load the pre-trained Haar Cascade face detection classifier.
2. Detect faces in images or video streams.

```python
import cv2

# Load pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
```

## Dependencies

- `opencv-python`
- `mediapipe`
- `jupyter`

You can install the necessary dependencies using pip:

```bash
pip install opencv-python mediapipe jupyter
```

## How to Run

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the scripts from the `basics/` folder to explore basic OpenCV functions.
4. Run `main.py` from the `Project_Virtual_Painter/` folder to start the virtual painting application.
5. Open the `face_detection.ipynb` Jupyter notebook to test face detection.


