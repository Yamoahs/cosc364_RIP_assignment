#########################################################################
# File: Timer.py
# Authors: SY, JL
# Date Created: 28/04/16
# Date Modified: 28/04/16
#########################################################################

import time
import sys

def update_timer(timer):
    t = timer
    while t != 0:
        time.sleep(1)
        t  -= 1
        print(t)


update_timer(5)


