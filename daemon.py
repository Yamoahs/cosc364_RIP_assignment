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
from connection import *
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
DEFAULT_UPDATE_TIMER = 1#5
DEFAULT_TIMEOUT_TIMER = 6#10 #180
DEFAULT_GARBAGE_TIMER = 8#15 #120

#### /END OF GLOBAL VARIABLES
################################################################################

def main():
    param = parser.get_params(args)
    router = Router(param)
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
    for route in router.neigbour_dist:
        table.add_route(route, router.neigbour_dist[route], route)
    table.print_table()
    update_timer.start()
    # router.send_data(table)
    while True:
        sleep(0.05)
        updated = False
        updated = table.route_timers()
        if update_timer.finished(): #general timer that keeps track of time for updates
            router.send_data(table)
            update_timer.reset()
        recieved = router.recv_data()
        for serial in recieved:
            # print("serial", serial)
            #try to update the table will all teh serial data
            updated = updated or table.update_table(serial, neighbour_ports, neigbour_dist)
        if updated: #triggered updates
            router.send_data(table)
            table.print_table()


if __name__ == "__main__":
    main()
    router.close_sockets()
