#########################################################################
# File: Timer.py
# Authors: SY, JL
# Date Created: 28/04/16
# Date Modified: 28/04/16
#########################################################################

import time
import sys

def update_timer(u_timer):
    t = u_timer
    #TODO may have to randomise the offset
    time.sleep(1) # Offset the update timer
    while t != 0:
        time.sleep(1)
        t  -= 1
        print(t)

def timeout(t_timer):
    # Timeout time = 180sec
    pass


def garbage_collection_timer(g_timer):
    #Garbage Timeout time =  120sec
    pass


update_timer(2)


#changed file
