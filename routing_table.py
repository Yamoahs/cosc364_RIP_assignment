################################################################################
# File: routing_table.py
# Author: sy, jl
# Date created: 5/05/17
# Date Modified: 05/05/17
# In Param:
# Out Param:
################################################################################
import sys
import os.path
import re
import connection
import socket
from time import sleep, time
from timer import *


class Routing_table(object):
    """Class Descriptor
    """

    def __init__(self, router_id, neighbour_dist, timeout, garbage):
        self.router_id = router_id
        self. neighbour_dist = neighbour_dist
        self.timeout = timeout
        self.garbage = garbage
        self.routes = {}

        # for neighbour in self.neighbour_dist:
        #     self.routes[neighbour] = \
        #                   (neighbour, self.neighbour_dist[neighbour], neighbour)
        #Add host router to routing table
        self.routes[int(self.router_id)] = (int(self.router_id), 0, int(self.router_id))

    def add_route(self):
        pass

    def add_entry(self, dest, cost, nxt_hop):
        """"Add new routing destination to the routing table"""
        self.routes[dest] = (dest, cost, nxt_hop)

    def del_entry(self, dest):
        """"Add new routing destination to the routing table"""
        del self.routes[dest]


    def print_table(self):
        label1 = "      Router {} Routing Table  {}  ".format(self.router_id,\
                  time.strftime('%H:%M:%S'))
        label2 = "|    Dest     |    Cost     |    Nxt.Hop    |"
        line =   "|___________________________________________|"

        print(label1)
        print(label2)
        print(line)
        for entry in sorted(self.routes.values()):
            print(" " * 5, entry[0], " " * 5 \
                 + " " * 6, entry[1], " " * 5 \
                 + " " * 6, entry[2], " " * 5)
        print(line)


    def update_table(self, serial, neighbours):
        pass



if __name__ == '__main__':
    r = {6: 24, 7: 34, 2:44}
    table = Routing_table(1, r)
    table.print_table()
    print(table.routes)
    table.add_entry(8,88,88)
    table.del_entry(6)
    table.print_table()
