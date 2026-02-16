import cv2

input_video = "videos/rugby.mp4"
output_video = "videos/rugby_short.mp4"

cap = cv2.VideoCapture(input_video)

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

max_seconds = 8
frame_limit = fps * max_seconds

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret or count >= frame_limit:
        break
    out.write(frame)
    count += 1

cap.release()
out.release()

print("Video trimmed successfully")
