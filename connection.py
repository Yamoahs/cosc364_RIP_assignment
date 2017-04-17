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

class Router_connection():
    """docstring for Router_connection."""
    def __init__(self, parameters):
        self.router_id, self.input_ports, self.output_ports, self.timer \
        = parameters
        self.input_sockets = {}

    def in_sockets(self):
        for i, port in enumerate(self.input_ports):
            #Create the sockets
            try:
                self.input_sockets['input {}'.format(i)]\
                = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            except socket.error as e:
                print(str(e))
        return self.input_sockets


    def display_router_config(self):
        print("Router ID: ", self.router_id)
        print("Input Ports: ", self.input_ports)
        print("Output Ports & metrics: ",self.output_ports)
        print("Custom Timer: ",self.timer)
        # in_sockets()
