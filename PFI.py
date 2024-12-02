from Radio import radio
from Motor import robot
from Orientation import Orient
import cv2


rad = radio()
rob = robot()
ort = Orient()
Run = True
PosCoord = { 
    "StartPos" : (0,0),
    "Pos2" : (10.45,0),
    "Pos3" : (10.14,8.10),
    "FinalPos" : (-0.47,7.74)  
}


while (Run):
    CurrentPos = rad.obtenir_position()


    key = cv2.waitKey(500)
    if (key == ord("q")):
        Run = False