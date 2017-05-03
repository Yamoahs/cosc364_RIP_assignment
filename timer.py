#########################################################################
# File: Timer.py
# Authors: SY, JL
# Date Created: 28/04/16
# Date Modified: 28/04/16
#########################################################################

import time
import sys

def update_timer(u_timer):
    print("update timer")
    t = u_timer
    #TODO may have to randomise the offset
    time.sleep(1) # Offset the update timer
    while t != 0:
        time.sleep(1)
        t  -= 1
        print(t)

def timeout(t_timer):
    # Timeout time = 180sec
    print("timeout timer")
    t = t_timer
    while t != 0:
        time.sleep(1)
        t  -= 1
        print(t)


def garbage_collection_timer(g_timer):
    #Garbage Timeout time =  120sec
    print("garbage collection timer")
    t = g_timer
    while t != 0:
        time.sleep(1)
        t  -= 1
        print(t)


update_timer(5)
timeout(5)
garbage_collection_timer(5)
