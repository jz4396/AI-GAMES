# create_training_data.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os

cv2.namedWindow("lel")

def main():
            # 800x600 windowed mode
            screen = grab_screen(region=(400,100,1000,300))
            cv2.imshow("lel",screen)
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (200, 68))
            cv2.imwrite("lol.jpg", screen);
            cv2.imshow("lel",screen)
            
            print("hi")



main()
