################################################################################
# File: daemon.py
# Author: sy, jl
# Date created: 15/04/17
# Date Modified: 04/05/17
################################################################################
import sys
import os.path
import re
import parser
import connection
import socket
from time import sleep, time

################################################################################
## Global variables
################################################################################
# Get the arguments list
args = (sys.argv)

#### /END OF GLOBAL VARIABLES
################################################################################

param = parser.get_params(args)
router = connection.Router(param)
router_id, input_ports, output_ports, timer, input_sockets, output_sockets,\
neigbour_dist, neighbour_ports = router.return_data()
data = "hello Reciever from router {}".format(router_id)

while True:
    # print(input_sockets)
    router.send_data(data)
    recieved = router.recv_data()
    print("\nrecieved data: ", recieved)



router.close_sockets()
