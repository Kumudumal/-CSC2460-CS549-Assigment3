import cv2
import os

video_path = "videos/baseball_short.mp4"
output_folder = "frames/baseball"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imwrite(f"{output_folder}/frame_{count:04d}.jpg", frame)
    count += 1

cap.release()

print("Total frames extracted:", count)
