# Use an appropriate base image with Python and OpenCV support
FROM pytorch/pytorch:latest

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Install necessary system packages
RUN apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 

RUN apt-get update && apt-get install -y \
    libxrender-dev \
    libgtk2.0-dev

RUN apt-get install -y \
    libxrender1 \
    libxtst6 \
    libgtk2.0-0

# Install Python packages
RUN pip install --upgrade pip && \
    pip install numpy pandas opencv-python-headless matplotlib ultralytics scikit-learn torchmetrics mlxtend


RUN apt-get install -y libgl1-mesa-glx

RUN adduser -u 5678 --disabled-password --gecos "" appuser && \
    adduser appuser video && \
    chown -R appuser /home/appuser
USER appuser
#install as a root
USER root

RUN apt install -y xterm
RUN apt install -y qt5-default

# Set the default working directory
WORKDIR /app

# Allow the container to access the X11 display and set DISPLAY environment variable
ENV DISPLAY=:0
#export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms
RUN export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/x86_64-linux-gnu/qt5/plugins/platforms
# Copy your course files to the working directory if needed
# COPY . /app

# Allow the container to access the webcam (add the "--device" flag)
# You may need to use "--privileged" mode or grant specific permissions
# depending on your host environment and security settings
#CMD ["python", "-c", "import cv2; print(cv2.VideoCapture(0).isOpened())"]
CMD while true; do echo "Hello, world!"; sleep 1; done
#CMD ["python", "/app/helmet/inference.py"]