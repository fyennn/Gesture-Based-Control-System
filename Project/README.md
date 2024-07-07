# Hand Gesture Controlled Slideshow
This project allows to control a slideshow using hand gestures detected via a webcam. The project uses OpenCV, MediaPipe, and CVZone libraries to detect hand gestures and PyAutoGUI to simulate keyboard presses.

## Features
- Detects hand gestures using a webcam
- Uses gestures to navigate a slideshow:
  - **[1, 1, 0, 0, 0]**: Next slide (right arrow key)
  - **[0, 0, 0, 0, 0]**: Previous slide (left arrow key)
  - **[1, 1, 1, 1, 1]**: Start slideshow (F5 key)
  - **[1, 1, 1, 0, 0]**: Exit slideshow (ESC key)

## Installation

### Prerequisites
- Python 3.7 or higher

### Install required libraries

1. **OpenCV**
    ```bash
    pip install opencv-python
    ```
2. **NumPy**
    ```bash
    pip install numpy
    ```
3. **PyAutoGUI**
    ```bash
    pip install pyautogui
    ```

4. **CVZone**
    ```bash
    pip install --user cvzone
    ```
5. **MediaPipe**
    ```bash
    pip install --user mediapipe
    ```