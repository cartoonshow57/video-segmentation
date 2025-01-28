import cv2
import numpy as np

video_file = "umcp.mpg"

cap = cv2.VideoCapture(video_file)

frames = []

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)
cap.release()

frames_array = np.array(frames)

print(frames_array[100][130][152]) # Check data