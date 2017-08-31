################################################################################
# File: connection.py
# Author: sy, jl
# Date created: 17/04/17
# Date Modified: 04/05/17
# In Param: Parsed router info from parser.py
# Out Param: Input Sockets, Output Sockets, neighbour distances & Ports
################################################################################
import os.path
import select
import socket
import struct
import sys

###############################################################################
## Global variables
################################################################################
#IP address
HOST =  "127.0.0.1"

#### /END OF GLOBAL VARIABLES
################################################################################


class Router(object):
    '''Class Descriptor'''
    def __init__(self, parameters):
        self.router_id, self.input_ports, self.output_ports, self.update_timer,\
                             self.timeout_timer, self.garbage_timer = parameters
        self.input_sockets = []
        self.output_sockets = {}
        self.neigbour_dist = {}
        self.neighbour_ports = {}

        #Create the input Sockets
        for port in self.input_ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                #Bind the sockets
                s.bind((HOST, port))
                self.input_sockets.append(s)
            except socket.error as e:
                print(str(e))

        #Create the output sockets and neighbour distances
        for output in self.output_ports:
            port, metric, nxt_hop = output
            #Create the sockets
            try:
                self.output_sockets[nxt_hop] =\
                socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            except socket.error as e:
                print(str(e))

            #neighbour distances & port
            self.neigbour_dist[nxt_hop] = metric
            self.neighbour_ports[nxt_hop] = port

    def send_data(self, data):
        # serialise = pack(data)
        for nxt_hop, socket in self.output_sockets.items():
            serial = data.serialize(nxt_hop)
            socket.sendto(serial, (HOST, self.neighbour_ports[nxt_hop]))

    def recv_data(self):
        available,_,_ = select.select(self.input_sockets, [], [], 0.1) # wait for 100ms, only interested in reading
        serials = []
        for socket in available:
            # print("sock", socket)
            data = socket.recv(1024)
            data = data.decode('utf-8')
            serials.append(data)
        return serials


    def close_sockets(self):
        for socket in self.input_sockets:
            socket.close()
        for socket in self.output_sockets:
            self.output_sockets[socket].close()

    def return_data(self):
        return self.router_id, self.input_ports, self.output_ports,\
        self.update_timer, self.timeout_timer, self.garbage_timer,\
        self.input_sockets, self.output_sockets, self.neigbour_dist,\
        self.neighbour_ports
