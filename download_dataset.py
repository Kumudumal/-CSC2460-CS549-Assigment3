from roboflow import Roboflow

rf = Roboflow(api_key="kyMWl2OBrol1fg8V1ykM")
project = rf.workspace("kumu").project("player-tracking-hndig")
version = project.version(2)
dataset = version.download("yolov8")

print("Dataset downloaded successfully")
