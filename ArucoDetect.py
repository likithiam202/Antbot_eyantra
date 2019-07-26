'''
* Team id       : eYRC #902
* Author List   : Karthik Raj S S
                  Jaffar Aleem
                  Likith S
                  Gagan L Naik
*Filename       : Aruco_detect
*Theme          : Ant Bot
*Functions      : used only in-built functions 
*Global Variables: camera,idlist,run
'''

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import cv2.aruco as aruco
import csv
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 64
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
idlist = []
run = True
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    if run:
        image = frame.array  

            

            #operations on frame

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)             #converting to grayscale
        aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)     #defining the dictionary in which the ids are present
            
        parameters = aruco.DetectorParameters_create()             #finding the parameters
        corners, ids, _ = aruco.detectMarkers(gray,aruco_dict , parameters = parameters)
        font = cv2.FONT_HERSHEY_SIMPLEX                            #font type
        cv2.putText(gray, "id = "+str(ids), (100,200), font, 1, (255,0,255), 2, cv2.LINE_AA) #to display the id on screen
            
     
            # show the frame
        cv2.imshow("Frame", gray)
        key = cv2.waitKey(1) & 0xFF
     
            # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        if len(corners):
            for i in range(len(corners)):
                if ids[i][0] not in idlist:
                    idlist.append(ids[i][0])    #appending the detected ids to the final list
                    if len(idlist) == 4:
                        run = False             #break after detecting all four ids
       
            
    else:
        break




cv2.destroyAllWindows()
print(idlist)                                   #printing the final idlist

#making a csv file
with open('eYRC#AB#902.csv','a',newline='') as fp:
                 a = csv.writer(fp,delimiter=',')
                 data = [['SIM0',idlist[0]],['SIM1',idlist[1]],['SIM2',idlist[2]],['SIM3',idlist[3]]]
                 a.writerows(data)
