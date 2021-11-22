# Face Recognition

# Importing the libraries
import cv2
import math

# Loading the cascades
face_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
color = (0, 0, 255)
scale = 0.4
thickness = cv2.FILLED
margin = 2


# Defining a function that will do the detections

def detect(gray, frame):
    posx = []
    posy = []
    dist = []
    j = 0
    i = 0
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 4)
        cv2.line(frame, (math.floor((x+x+w)/2),y), (math.floor((x+x+w)/2), math.floor((y+h+y+h)/2)), (127,0,255), 2)
        cv2.circle(frame, (math.floor((x+x+w)/2),y), 2, (127,0,255), 2)
        cv2.putText(frame, str(j), (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, scale, color, 1, cv2.LINE_AA)
        j = j+1
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #print(x,y,w,h)
        x = math.floor((x+x+w)/2)
        y = math.floor((y+h+y+h)/2)
        posx.append(x)
        posy.append(y)

    for x in posx:
        print(i)
        x1 = posx[0]
        x2 = posx[i]
        y1 = posy[0]
        y2 = posy[i]
        i = i+1
        if i>j:
            break
        #print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
        dist.append(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

    print(dist)
    greencolor = (0, 255, 0)
    k = 0
    badFlag = 1
    for x in dist:
       if dist[k] < 250 and dist[k] != 0:
            cv2.putText(frame, "NO SOCIAL DISTANCING", (40, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)
            badFlag = 3
            break
       k = k+1
       if k>j:
           break

    if badFlag < 2:
        cv2.putText(frame, "GOOD SOCIAL DISTANCING", (40, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.8, greencolor, 2, cv2.LINE_AA)

    dist.clear()
    posy.clear()
    txta = "without loop"
    return frame

# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()