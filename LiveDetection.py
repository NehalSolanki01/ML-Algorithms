import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0)

while(True):
    ret,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Webcam",frame)
    if cv2.waitKey(25)==32:
        break
vid.release()
cv2.destroyAllWindows


#Write a python script to detect pedestrian in a traffic scenario image/video. 
# Add eye detection code in Livedetection program