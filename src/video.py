import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('=' * 30) 
    print('Error: Camera is not detected.')
    print('=' * 30)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera Feed (Press Q to Close)", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()