from getkeys import key_check
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D

SPACE = 0x39

paused = False

while(True):
    if not paused:
        keys = key_check()

        if ' ' in keys:
            PressKey(SPACE)
            print("1")
        else:
            ReleaseKey(SPACE)
            print("0")
    if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
