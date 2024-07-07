import cv2
import numpy as np
import time
import pyautogui
from cvzone.HandTrackingModule import HandDetector

# Define the width and height of the camera frame
width, height = 800, 600

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Initialize the hand detector
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Define gesture cooldown time and threshold
gestureCooldown = 1  # Cooldown time in seconds
gestureTreshold = 150  # Example threshold value

# Initialize the time tracked
timeTracked = time.time()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(fingers)

        if time.time() >= timeTracked + gestureCooldown:
            if fingers == [1, 1, 0, 0, 0]:
                pyautogui.press('right')
                print("Pressing Right.")
                timeTracked = time.time()
            elif fingers == [0, 0, 0, 0, 0]:
                pyautogui.press('left')
                print("Pressing Left.")
                timeTracked = time.time()
            elif fingers == [1, 1, 1, 1, 1]:
                pyautogui.press('f5')
                print("Go to SlideShow.")
                timeTracked = time.time()
            elif fingers == [1, 1, 1, 0, 0]:
                pyautogui.press('esc')
                print("Escape SlideShow.")
                timeTracked = time.time()

    cv2.imshow("image", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
