import time

class Timers(object):

    def __init__(self):
        """ Set up some basics such as a collection of timers that you can use to
            store all the info. The details are for you to work out. I recommend
            you do not store duration, but end-time: it makes calculations easier.
        """
        pass

    def add_timer(self, duration, id, message):
        """ Add a timer of the given duration and (unique) ID.
            It should also have some information stored with it.
        """
        pass

    def remove_timer(self, id):
        """ The timer with the given ID should be removed. That’s it really."""
        pass

    def get_timeout(self):
        """ Calculate the amount of time left until the next timer will go off.
            If there are no timers left, that’s probably a bug.
            Also, experience tells me that you don’t need to store anything
            about which timer will expire, but you can if you wish.
        """
        pass

    def get_expired_timers(self):
        """ A list of (id, message) tuples should be returned,
            each of which belong to a timer that has expired since the last time
            this function was called. It should also remove them from the collection.
        """
        pass


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
