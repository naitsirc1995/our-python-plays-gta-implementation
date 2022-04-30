from pickle import NONE
import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, W, A, S, D
import pyautogui


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_or(img, mask)
    return masked

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 90, threshold2=300)
    #vertices = np.array([[10,500],[10,300], [300,200], [500,200], [800,300], [800,500]], np.int32)
    #processed_img = roi(processed_img, [vertices])
    return processed_img

def main():    
    last_time = time.time()
    pyautogui.click(100,150)     
    i = 0     
    while True:                
        screen =  np.array(ImageGrab.grab(bbox=(0,60,800,600)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        winname = "juego"
        cv2.namedWindow(winname)
        cv2.moveWindow(winname,800,900)
        new_screen = process_img(screen)
        cv2.imshow(winname, new_screen)
        cv2.setWindowProperty("game",cv2.WND_PROP_TOPMOST,2)
        if i == 0:
            #pyautogui.hotkey('alt', 'tab') #alt + tab linux
            time.sleep(2)
            pyautogui.click((120,120))
            
            
        i+=1
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB) )
        if cv2.waitKey(25) & 0xFF == ord('q'):            
            cv2.destroyAllWindows()
            break



if __name__ == '__main__':
    main()