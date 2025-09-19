import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Flip the frame horizontally (mirror image)
    # Use 0 for vertical flip, 1 for horizontal flip, -1 for both
    flipped_frame = cv2.flip(frame, 1)

    # Display the original and flipped frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Flipped Frame', flipped_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()