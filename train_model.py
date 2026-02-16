from ultralytics import YOLO

# load model (pretrained small model)
model = YOLO("yolov8n.pt")

# train on your dataset
model.train(
    data="player-tracking-2/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8
)

print("Training Finished")

