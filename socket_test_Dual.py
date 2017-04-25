import socket
import select
import time
import sys
import os.path

# Get the arguments list
args = (sys.argv)

HOST = "127.0.0.1"
data = "Hello from router {}".format(args[1])
# PORTA = 2025
# PORTB = 2026
#
#
# inputt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# output = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# #Bind input on either end to listen
# inputt.bind((HOST, PORTA))
# output.bind((HOST, PORTB))
#
# def send_data(socket, data, port):
#     socket.sendto(data.encode('utf-8'), (HOST, port))
#     print("sent ", data)
#
# def recv_data(socket):
#     available = select.select(socket, [], [], 0.1) # wait for 100ms, only interested in reading
#     data = socket.recv(1024)
#     print(data.decode('utf-8'))


#
# while True:
#     if args[1] == 1:
#         send_data(output, data, PORTA)
#     else:
#         send_data(output, data, PORTB)
#     time.sleep(1)
#     if args[1] == 2:
#         recv_data(inputt)
#     else:
#         recv_data(output)
# router-id 1
# input-ports 1025, 1026, 1027
# output-ports 2025-1-2, 6026-5-6, 7025-8-7


class Router:
    '''Class Descriptor'''
    def __init__(self, parameters):
        self.router_id, self.input_ports, self.output_ports, self.timer \
        = parameters
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
            port, metric, next_hop = output
            #Create the sockets
            try:
                self.output_sockets[next_hop] =\
                socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                # #Connect the sockets
                # self.output_sockets[next_hop].connect((HOST, port))
            except socket.error as e:
                print(str(e))

            #neighbour distances & port
            self.neigbour_dist[next_hop] = metric
            self.neighbour_ports[next_hop] = port

    def send_data(self, data):
        for out_sock in self.output_sockets:
        out_sock.sendto(data.encode('utf-8'), (HOST, neighbour_ports[out_sock]))
        print("sent ", data)

    def recv_data(self):
        available = select.select(socket, [], [], 0.1) # wait for 100ms, only interested in reading
        data = available.recv(1024)
        print(data.decode('utf-8'))
