import cv2
from collections import deque

def draw_marker(frame, cen: tuple,):
    cv2.circle(frame, cen, 8, (0, 0, 255), -1)


def draw_trail(frame, trail: tuple):
    for i in range(1, len(trail)):
        alpha = 1 - (i/len(trail))
        overlay = frame.copy()
        cv2.line(frame, trail[i-1], trail[i], (0, 0, 255), 2)
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)