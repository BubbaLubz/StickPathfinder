import cv2
from collections import deque

def draw_marker(frame, cen: tuple,):
    cv2.circle(frame, cen, 8, (0, 0, 255), -1)


def draw_trail(frame, trail: tuple):
    for i in range(1, len(trail)):
        cv2.line(frame, trail[i-1], trail[i], (0, 0, 255), 2)