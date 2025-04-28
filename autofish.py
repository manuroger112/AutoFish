import winsound
import win32api
import numpy as np
import easyocr
import random
import time 
import cv2
import mss

region = {"top": 750, "left": 1600, "width": 300, "height": 300}
        
screenCapture = mss.mss()
reader = easyocr.Reader(['en'])

MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010

def pressRightMouse():
    win32api.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

while True:
    time.sleep(0.8)
    frame = np.array(screenCapture.grab(region))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
    detectionResult = reader.readtext(frame)
    
    if win32api.GetAsyncKeyState(0x06) < 0:
        break
    for i in range(len(detectionResult)):
        text = detectionResult[i][1]
        print(text.lower()) 
        if text.lower() == "fishing bobber splashes":
            pressRightMouse()
            time.sleep(random.randint(2, 11) * 0.01)
            pressRightMouse()
            
print("bye")
winsound.Beep(1000, 50)





#----------------DEBUG-----------------------#
#print(text.lower()) 
#cv2.imshow('screen', frame)

    #if (cv2.waitKey(1) & 0xFF) == ord('q'):
        #cv2.destroyAllWindows()
        #break
