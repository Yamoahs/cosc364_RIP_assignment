import socket
import select
import time
import sys
import os.path

# Get the arguments list
args = (sys.argv)

HOST = "127.0.0.1"


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
        for next_hop, socket in self.output_sockets.items():
            socket.sendto(data.encode('utf-8'), (HOST, self.neighbour_ports[next_hop]))
            print("sent: ", data)

    def recv_data(self):
        available,_,_ = select.select(self.input_sockets, [], []) # wait for 100ms, only interested in reading
        serials = []
        for socket in available:
            # print("sock", socket)
            # serials.append(self.read_data(socket))
            data = socket.recv(1024)
            serials.append(data.decode('utf-8'))
        return serials
            # print(data.decode('utf-8'))

    # def read_data(self, in_socket):
    #     data = in_socket.recv(1024)
    #     return data.decode('utf-8')

    def close_sockets(self):
        for socket in self.input_sockets:
            socket.close()
        for socket in self.output_sockets:
            self.output_sockets[socket].close()

    def return_data(self):
        return self.router_id, self.input_ports, self.output_ports, self.timer,\
        self.input_sockets, self.output_sockets, self.neigbour_dist,\
        self.neighbour_ports
