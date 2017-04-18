################################################################################
# File: connection.py
# Author: sy, jl
# Date created: 17/04/17
# Date Modified: 17/04/17
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


class Router_connection():
    """docstring for Router_connection."""
    def __init__(self, parameters):
        self.router_id, self.input_ports, self.output_ports, self.timer \
        = parameters
        self.input_sockets = {}

    def in_sockets(self):
        for i, port in enumerate(self.input_ports):
            for neighbour in self.output_ports:
                #Create the sockets
                try:
                    self.input_sockets[i] =\
                    socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                    #Bind the sockets
                    self.input_sockets[i].bind((HOST, port))

                    #Connect the sockets
                    self.input_sockets[i].connect((HOST, neighbour[0]))

                except socket.error as e:
                    print(str(e))

        return self.input_sockets

    def close_sockets(self):
        for socket in self.input_sockets:
            self.input_sockets[socket].close()


    def display_router_config(self):
        print("Router ID: ", self.router_id)
        print("Input Ports: ", self.input_ports)
        print("Output Ports & metrics: ", self.output_ports)
        print("Custom Timer: ",self.timer)
        print("\n Input Sockets:\n", self.input_sockets)
        # in_sockets()
