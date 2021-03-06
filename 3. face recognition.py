

from typing import Counter
import cv2
import numpy as np
import os
import time
import pyrebase
import datetime
import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
buzzer=16
GPIO.setup(buzzer,GPIO.OUT)



GPIO.setup(3, GPIO.IN)

firebaseConfig={
    'apiKey': "AIzaSyBSeEACcuzg9rayivf2Hcq22vbLMQ8z-bg",
    'authDomain': "home-security-87542.firebaseapp.com",
    'databaseURL': 'https://home-security-87542-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'projectId': "home-security-87542",
    'storageBucket': "home-security-87542.appspot.com",
    'messagingSenderId': "28838967093",
    'appId': "1:28838967093:web:5695da119ff115c9fb3e7c",
    'measurementId': "G-2WZNDVF365"
}

firebase=pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
while(True):
    val = GPIO.input(3)
    print(val)
    if(val==0):
        print("here")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')   #load trained model
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath) #to identify faces

        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter, the number of persons you want to include
        id = 2 #two persons (e.g. Jacob, Jack)


        names = ['','anurag']  #key in names, start from the second place, leave first empty

        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        flag = True
        flag2= False
        counter_known=0
        counter_gap=0

        while flag:

            ret, img =cam.read()

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )
            val = GPIO.input(3)
            if( val==1):
                flag2=True
            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                cf=0
                # Check if confidence is less them 100 ==> "0" is perfect match 
                if (confidence < 100):
                    id = names[id]
                    cf=round(100-confidence)
                    confidence = "  {0}%".format(round(100 - confidence))
                    if(cf>30):
                        counter_known=counter_known+1
                    else:
                        counter_gap=counter_gap+1
                    

                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                    counter_gap=counter_gap+1
                
                #print(id)
                   
                
                now = datetime.datetime.now()
                date=now.strftime("%d-%m-%y")
                currentTime=now.strftime("%H:%M:%S")
                if( counter_known> 100 and counter_gap <=20):
                    
                    flag2=True
                    print("counter known :"+str(counter_known))
                    print("\n counter gap :"+str(counter_gap))
                    data={"alert":"allow" , "person":id,"date":date , "time":currentTime}
                    db.push(data)
                    
                    
                    break
                elif counter_gap >100:
                    print("876742")
                    print("counter known :"+str(counter_known))
                    print("\n counter gap :"+str(counter_gap))
                    data={"alert":"stranger, notify" ,"person":"unknown","date":date , "time":currentTime}
                    GPIO .output(buzzer,GPIO.HIGH)
                    sleep(5)
                    GPIO.output(buzzer,GPIO.LOW)
                    db.push(data)
                    counter_gap=0
                    counter_known=0
                elif (counter_known >100 and 20<counter_gap<100):
                    
                    print("counter known :"+str(counter_known))
                    print("\n counter gap :"+str(counter_gap))
                    data={"alert":"cannot allow, try again" ,"person":"unknown","date":date , "time":currentTime}
                    
                    db.push(data)

                    counter_gap=0
                    counter_known=0

                if(cf>30):
                    cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                    cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
                else:
                    cv2.putText(img, "unknown", (x+5,y-5), font, 1, (255,255,255), 2)
                    cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
                    
            if(flag2):
                break
            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()
        time.sleep(7)
        ini_t= time.time()
        while(True):
            if(time.time()-ini_t >5):               
                break
    else:
        print("out")
        cv2.destroyAllWindows()


