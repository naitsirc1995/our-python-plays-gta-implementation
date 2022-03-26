import numpy as np
from PIL import ImageGrab
import cv2
import time






def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
        # 40 px accounts for title bar. 
        printscreen =  np.array(ImageGrab.grab(bbox=(150,0,1200,640)))
        printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
        printscreen =  cv2.Canny(image=printscreen, threshold1=100, threshold2=200)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',printscreen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
