import numpy as np
import cv2

watch_cascade = cv2.CascadeClassifier('watch_cascade.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    watches = watch_cascade.detectMultiScale(gray)
    for (x,y,w,h) in watches:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2, cv2.LINE_AA)
    cv2.imshow("Watch",frame)
    if len(watches) != 0:
        print(len(watches))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
