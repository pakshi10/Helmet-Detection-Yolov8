from ultralytics import YOLO
import cv2

# Load a pretrained YOLOv8n model
model = YOLO('/app/helmet/runs/detect/train/weights/best.pt')

# Define path to video file
source = '/app/helmet/video/output.avi'

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
cap = cv2.VideoCapture(source)

# Get the frame dimensions from the video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create VideoWriter object
output_resolution = (frame_width, frame_height)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, output_resolution)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Write the frame to the output video
        out.write(annotated_frame)


        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
