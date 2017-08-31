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
from route import Route
from serialise import *


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
        #                   Route(neighbour, self.neighbour_dist[neighbour],\
        #                                   neighbour, self.timeout, self.garbage)
        # Add host router to routing table
        # self.routes[int(self.router_id)] = (int(self.router_id), 0, int(self.router_id))
        # self.routes[self.router_id] = Route(int(self.router_id), 0, int(self.router_id),\
        #                                              self.timeout, self.garbage)

    def add_route(self, dest, cost, nxt_hop):
        """"Add new routing destination to the routing table"""
        route = self.routes.get(dest, None)
        change = False
        if route: # Update existing route
            change = change or route.update(nxt_hop, cost)
        else:
            # don't add yourself or routes through yourself
            if dest != self.router_id and nxt_hop != self.router_id:
                self.routes[dest] = Route(dest, cost, nxt_hop, self.timeout, self.garbage)
                change = True
        return change

    def print_table(self):
        label1 = "      Router {} Routing Table  {}  ".format(self.router_id,\
                  time.strftime('%H:%M:%S'))
        label2 = "|    Dest     |    Cost     |    Nxt.Hop    |"
        line =   "|___________________________________________|"

        print(label1)
        print(label2)
        print(line)
        # for route in self.routes.values():
        for route in sorted(self.routes.values(), key=lambda route: route.dest):
            print( " " * 5, route.dest, " " * 5 \
                 + " " * 6, route.cost, " " * 5 \
                 + " " * 6, route.nxt_hop, " " * 5)
        print(line)

    def serialize(self, sendto_router_id): ###Change to pack
        serial = "{}:".format(self.router_id)
        # for route in self.routes.values():
        for route in sorted(self.routes.values(), key=lambda route: route.dest):
            # split horizon poisoned reverse
            cost = 16 if route.nxt_hop == sendto_router_id else route.cost
            serial += "{},{},{}|".format(route.dest, cost, route.nxt_hop)
        return bytes(serial[:-1], 'utf-8') # remove last |, encode as bytes in utf-8

    def update_table(self, serial, neighbours, neigh_dist):
        recv_data = unpack(serial)
        # print("recv_data",recv_data)
        change = False
        if recv_data:
            sentfrm_router_id = int(recv_data[0])
            routes = recv_data[1]
            sender = self.routes.get(sentfrm_router_id, None)
            # Check if serial data is a Neighbour and not already in the routing table
            neighbour = neigh_dist.get(sentfrm_router_id, None)
            if not sender and neighbour:
                self.add_route(sentfrm_router_id, neigh_dist[sentfrm_router_id]\
                                                                 ,sentfrm_router_id)
                # self.add_route(sentfrm_router_id, neighbour_dist[sentfrm_router_id]\
                #                                                  ,sentfrm_router_id)
                sender = self.routes.get(sentfrm_router_id, None)
            if sender:
                sender.update(sender.nxt_hop, sender.cost)
                for dest, cost, nxt_hop in routes:
                    if nxt_hop != self.router_id: # don't add routes through self
                        change = change or self.add_route(int(dest), int(cost)\
                                          + int(sender.cost), int(sentfrm_router_id))
        return change
        # for node in serial:
        #     dst, metric, nxt_hop = serial[node]
        #     # Check if serial data is a Neighbour and hasnt already been added
        #     # to the routing table
        #     if node in neighbours.keys() and node not in routes.keys():
        #         dest, metric, next_hop = node, neighbour_dist[node], node
        #         self.add_route(dest, metric, next_hop)
        #     elif node not in routes.keys():
        #         self.add_route(dst, metric, nxt_hop)
        #

    def route_timers(self):
        routes = {}
        change = False
        for dest, route in self.routes.items():
            if not route.garbage.finished(): # if garbage is done it will be removed
                routes[dest] = route
                if route.timeout.finished():
                    route.start_garbage()
                    change = True
            else:
                change = True
        self.routes = routes
        return change


if __name__ == '__main__':
    r = {6: 24, 7: 34, 2:44}
    table = Routing_table(1, r)
    table.print_table()
    print(table.routes)
    table.add_route(8,88,88)
    table.del_entry(6)
    table.print_table()
