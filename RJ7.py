from ultralytics import YOLO
model = YOLO("yolov8x.pt")
results = model("/content/drive/MyDrive/sample.mp4", save=True, save_txt=True, save_conf=True)
boxes = results[0].boxes
for box in boxes:
 print(box.data)
print(results[0].names)