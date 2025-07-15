# webcam_utils.py

import cv2

def capture_webcam_image(filename="captured_image.jpg"):
    """Captures an image from the webcam and saves it."""
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return False, "Error: Could not access the webcam."

    ret, frame = cap.read()

    if ret:
        cv2.imwrite(filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
        cap.release()
        cv2.destroyAllWindows()
        return True, filename
    else:
        cap.release()
        cv2.destroyAllWindows()
        return False, "Error: Failed to capture image."
