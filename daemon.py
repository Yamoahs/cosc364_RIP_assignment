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

################################################################################
## Global variables
################################################################################
# Get the arguments list
args = (sys.argv)

# Default Timers
DEFAULT_UPDATE_TIMER =30

#### /END OF GLOBAL VARIABLES
################################################################################

param = parser.get_params(args)
router = connection.Router(param)
router_id, input_ports, output_ports, timer, input_sockets, output_sockets,\
neigbour_dist, neighbour_ports = router.return_data()
data = "hello Reciever from router {}".format(router_id)
update_timer = Timers(10, 1, "update timer")
timer_id, duration, label, running = update_timer.return_info()
update_timer.start()

runs = 0
router.send_data(data)
while True:

    sleep(0.05)
    # print(input_sockets)
    print("Router: {} run: {}\n".format(router_id, runs))
    print(time.strftime('%H:%M:%S'))
    # router.send_data(data)
    if update_timer.finished():
        print("got here")
        router.send_data(data)
        runs += 1
        update_timer.reset()
        print(label, " complete. start again")
        recieved = router.recv_data()
        print("\nrecieved data: ", recieved)
    print("Still waiting")



router.close_sockets()
