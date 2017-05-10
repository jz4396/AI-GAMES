# test_model.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D
from alexdino import alexnet
from getkeys import key_check

import random

SPACE = 0x48

WIDTH = 200
HEIGHT = 68
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'pydinoimbalance-fast-{1}-{1}-{1}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.09

def Jump():
##    if random.randrange(4) == 2:
##        ReleaseKey(W)
##    else:
    PressKey(SPACE)
    
def noJump():
    ReleaseKey(SPACE)

    
model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # 800x600 windowed mode
            screen = grab_screen(region=(400,100,1000,300))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (200, 68))

            prediction = model.predict([screen.reshape(200,68,1)])[0]
            print(prediction)

            Jump_thresh = 0.50

            if prediction[0] > Jump_thresh:
                Jump()
            else:
                noJump()

        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

main()       










