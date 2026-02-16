from ultralytics import YOLO

# load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# track players in a video
model.track(
    source="videos/cricket.1.mp4",
    show=True,
    conf=0.3,
    save=True
)
