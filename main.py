import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
from directkeys import PressKey, W, A, S, D
import pyautogui



def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def main():    

    last_time = time.time()
    pyautogui.click(100,150)     
    i = 0     
    while True:        
        PressKey(W)
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('Frame took {} seconds'.format(time.time()-last_time))        
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)                
        if i == 0:            
            #pyautogui.hotkey('alt', 'tab') #alt + tab linux
            time.sleep(2)
            pyautogui.click((1500,150))
            print("I was just clicked")
        i+=1
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB) )
        if cv2.waitKey(25) & 0xFF == ord('q'):            
            cv2.destroyAllWindows()
            break



if __name__ == '__main__':
    main()