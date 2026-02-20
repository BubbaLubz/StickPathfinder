import cv2 as cv
import numpy as np

# OpenCV HelloWorld test

print("OpenCV:", cv.__version__)

# creates a blank black image as a NumPy array.  Dimennsions are 120x400.  np.zeros fills every pixel with 0 (black). 
# dtype=np.uint8 means each channel value is an integer 0-255.
img = np.zeros((120, 400, 3), dtype=np.uint8)   

cv.putText(img, "PEENAR", (10, 80), cv. FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3) # (10,80) is where the text starts.  
cv.imwrite("hello.png", img)