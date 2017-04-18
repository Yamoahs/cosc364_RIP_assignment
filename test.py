import sys
import os.path
import re
import parser
import connection
import socket

# Get the arguments list
args = (sys.argv)
# while True:
print("hello")
param = parser.get_params(args)

router = connection.Router_connection(param)


router.in_sockets()
info = router.display_router_config()
router_id, input_ports, output_ports, timer, input_sockets = info

data = "hello Reciever from router {}".format(router_id)
while True:
    for neighbour in input_sockets:
        print(neighbour)
        indat = input_sockets[neighbour].recv(512)
        print(indat.decode('utf-8'))
        input_sockets[neighbour].send(data.encode('utf-8'))


print(data)
    # sender_out_socket.send(data.encode('utf-8'))
    # data = sender_in_socket.recv(512)
    # print("From Reciever: ", data.decode('utf-8')

router.close_sockets()
