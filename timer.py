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


# update_timer(5)
# timeout(5)
# garbage_collection_timer(5)

class Timers(object):

    def __init__(self, duration, tag, label):
        """ Set up some basics such as a collection of timers that you can use to
            store all the info. The details are for you to work out. I recommend
            you do not store duration, but end-time: it makes calculations easier.
        """
        self.time = None
        self.tag = tag
        self.duration = duration
        self.label = label
        self.running = False


    # def add_timer(self, duration, id, message):
    #     """ Add a timer of the given duration and (unique) ID.
    #         It should also have some information stored with it.
    #     """
    #     pass
    #
    # def remove_timer(self, id):
    #     """ The timer with the given ID should be removed. That’s it really."""
    #     pass
    #
    # def get_timeout(self):
    #     """ Calculate the amount of time left until the next timer will go off.
    #         If there are no timers left, that’s probably a bug.
    #         Also, experience tells me that you don’t need to store anything
    #         about which timer will expire, but you can if you wish.
    #     """
    #     pass
    #
    # def get_expired_timers(self):
    #     """ A list of (id, message) tuples should be returned,
    #         each of which belong to a timer that has expired since the last time
    #         this function was called. It should also remove them from the collection.
    #     """
    #     pass

    def start(self):
        """Set the running flag to True"""
        self.time = time.time()
        self.running = True

    def stop(self):
        """Set the running flag to False"""
        self.running = False

    def reset(self):
        """Reset the clock ready for next use"""
        self.time = time.time()

    def get_timeout(self):
        """ Calculate the amount of time left until the next timer will go off.
        """
        return ((self.time + self.duration) - time.time())


    def finished(self):
        """Checks if the timer has reached it's duration time"""
        if self.running and time.time() >= (self.time + self.duration):
            self.running = False
        return self.running and time.time() >= (self.time + self.duration)

    def return_info(self):
        """Returns timer information"""
        return self.tag, self.duration, self.label, self.running


if __name__ == '__main__':
    t = Timers()
    t.add_timer(5, 't1', "update")  # Easily parsible messages
    t.add_timer(7, 't2', "gc-r6")

    while True:
        wait = t.get_timeout()
        if wait is None:
            break  # No more timers. This might be handled by an exception.
        time.sleep(wait)
        for tid, message in t.get_expired_timers():
            print("Timer", tid, "fired!")
            print("   ", message)
