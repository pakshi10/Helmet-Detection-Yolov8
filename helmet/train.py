from ultralytics import YOLO
from IPython.display import display, Image

print("Loading model...")

# Load model
# This is detection model
model = YOLO(f'../helmet/model/yolov8n.pt')
#Test the model on a image
results = model.predict(source='https://media.roboflow.com/notebooks/examples/dog.jpeg', conf=0.25)

# Display results
print("Boxes:",results[0].boxes.xyxy[0])
print("Confidence:",results[0].boxes.conf)
print("Class:",results[0].boxes.cls)

# dataset location
dataset_yaml = '/app/helmet/dataset/helmet_data/data.yaml'
dataset = '../helmet/dataset/'
# Train the model
# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data=dataset_yaml, epochs=10,batch=2,imgsz=640)

# Evaluate the model's performance on the validation set
results = model.val()




