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
from timer import *
from routing_table import *

################################################################################
## Global variables
################################################################################
# Get the arguments list
args = (sys.argv)

# Default Timers
DEFAULT_UPDATE_TIMER = 5
DEFAULT_TIMEOUT_TIMER = 180
DEFAULT_GARBAGE_TIMER = 120

#### /END OF GLOBAL VARIABLES
################################################################################

param = parser.get_params(args)
router = connection.Router(param)
router_id, input_ports, output_ports, update_timer, timeout_timer,\
garbage_timer, input_sockets, output_sockets, neigbour_dist, neighbour_ports = \
                                                            router.return_data()
##Set the timeout and garabage timer if not specified in the config file
if not timeout_timer:
    timeout_timer = DEFAULT_TIMEOUT_TIMER

if not garbage_timer:
    garbage_timer = DEFAULT_GARBAGE_TIMER

if not update_timer:
    update_timer = Timers(DEFAULT_UPDATE_TIMER)
else:
    update_timer = Timers(update_timer)

table = Routing_table(router_id, neigbour_dist, timeout_timer, garbage_timer)
# data = "hello Reciever from router {}".format(router_id)
data = table.routes
update_timer.start()

router.send_data(data)
table.print_table()
while True:
    sleep(0.05)
    if update_timer.finished():
        data = table.routes
        table.print_table()
        router.send_data(data)
        update_timer.reset()
        recieved = router.recv_data()
        print("\nrecieved data: ", recieved)



router.close_sockets()
