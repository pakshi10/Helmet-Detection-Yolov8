# Helmet-Detection-Yolov8
Detection of helmet using custom data from Yolov8.

## Yolov8
One of the key innovations in YOLOv8 is its use of anchor-free detection. This means that YOLOv8 does not need to pre-define anchor boxes, which can be a complex and time-consuming process. Instead, YOLOv8 predicts the center of an object directly, which leads to faster and more accurate detections.

## Installation
Docker : Make sure you have docker and docker compose on your system.

Installation of Docker : https://docs.docker.com/engine/install/

Installation of Docker compose : https://docs.docker.com/compose/install/

### Clone this repo
```
git clone https://github.com/pakshi10/Helmet-Detection-Yolov8.git
```

### Go inside directory
```
cd Helmet-Detection-Yolov8
```
### Build
```
sudo docker-compose up
```
### If the docker is build completely . You will get container name. Open a new terminal and go inside docker.
```
sudo docker exec -it container_name bash
```

