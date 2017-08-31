################################################################################
# File: route.py
# Author: sy, jl
# Date created: 15/04/17
# Date Modified: 04/05/17
################################################################################
import timer

class Route(object):

    def __init__(self, dest, cost, nxt_hop, timeout, garbage):
        self.dest = dest
        self.nxt_hop = nxt_hop
        self.cost = min(16, cost)
        self.timeout = timer.Timers(timeout)
        self.garbage = timer.Timers(garbage)
        self.timeout.start() # begin the timeout timer from the get go

    def __str__(self):
        return "(Destination: {}, cost: {}, nxt hop: {})".format(self.dest, \
        self.cost, self.nxt_hop)

    def update(self, nxt_hop, cost):
        changed = False
        # only update if new cost is smaller or if the original throughput
        # is the updater
        if cost < self.cost or self.nxt_hop == nxt_hop:
            changed = cost != self.cost
            self.nxt_hop = nxt_hop
            self.cost = min(16, cost)
            self.timeout.reset()
        if self.cost >= 16:
            self.garbage.start()
        else:
            self.timeout.start()
        return changed

    def start_garbage(self):
        self.cost = 16 # set cost to infinity
        self.timeout.stop() # make sure timeout has stopped
        self.timeout.reset() # reset both timers
        self.garbage.reset()
        self.garbage.start() # start garbage timer
