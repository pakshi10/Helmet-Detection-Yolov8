import os
import cv2

# Set a dummy DISPLAY environment variable
os.environ['DISPLAY'] = ':0'
# Set the QT_X11_NO_MITSHM environment variable
os.environ['QT_X11_NO_MITSHM'] = '1'

# Check if the DISPLAY environment variable is set
if 'DISPLAY' in os.environ:
    print("X11 is available. DISPLAY:", os.environ['DISPLAY'])
else:
    print("X11 is not available.")

import cv2

# Initialize the webcam (0 indicates the default camera)
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_resolution = (640, 640)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, output_resolution)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Resize the frame to the desired resolution (640x640)
    frame = cv2.resize(frame, output_resolution)

    # Write the frame to the output file
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Recording', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()




