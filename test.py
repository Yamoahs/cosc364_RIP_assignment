import sys
import os.path
import re
import parser
import connection
import socket
from time import sleep, time

# Get the arguments list
args = (sys.argv)
# while True:
print("hello")
param = parser.get_params(args)

router = connection.Router_connection(param)


# router.in_sockets()
# router.out_sockets()
info = router.display_router_config()
router_id, input_ports, output_ports, timer, input_sockets, output_sockets, neigbour_dist = info

print(output_ports)
print(output_sockets)

# data = "hello Reciever from router {}".format(router_id)


# while True:
#     for i in output_sockets:
#         output_sockets[i].send(data.encode('utf-8'))
#     for neighbour in input_sockets:
#         # print(neighbour)
#         indat = input_sockets[neighbour].recv(512)
#         print(indat.decode('utf-8'))

while(True):
    sleep(0.05)
    serials = router.recieve_data()
    router.send_table()



# print(data)
    # sender_out_socket.send(data.encode('utf-8'))
    # data = sender_in_socket.recv(512)
    # print("From Reciever: ", data.decode('utf-8')

router.close_sockets()
