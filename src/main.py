import cv2
import numpy as np
from collections import deque
from utils import draw_marker, draw_trail
from tracker import find_marker

if __name__ == "__main__":

    lower1 = np.array([0,100,100])
    upper1 = np.array([10,255,255])
    lower2 = np.array([170,100,100])
    upper2 = np.array([179,255,255])
    trail = deque(maxlen=50)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('Error: Camera is not detected.')
        exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        result = find_marker(frame, lower1, upper1)
        if result is None:
            result = find_marker(frame, lower2, upper2)

        if result is not None:
            cx, cy = result
            trail.append((cx,cy))
            draw_marker(frame, (cx, cy))
            draw_trail(frame, trail)

        cv2.imshow("StickPathfinder (Press Q to Close)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()








