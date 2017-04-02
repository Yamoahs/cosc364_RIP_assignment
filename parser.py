################################################################################
# File: parser.py                                              
# Author: sy, jl
# Date created: 27/03/17
# Date Modified: 3/04/17
################################################################################
import sys
import os.path

################################################################################
## Global variables
################################################################################

#IP address
HOST =  "127.0.0.1"

#valid Port no.
VALID_PORTS =  range(1024, 64001)

# Get the arguments list
args = (sys.argv)

#Flag to make sure stdin arguemtents
stdin_successful = False


#### /END OF GLOBAL VARIABLES

if len(args) == 5:
    if len(args) != len(set(args)):
        print("Duplicate Port Numbers")
        quit()
    for port in args[1:-1]:
        if int(port) not in VALID_PORTS:
            print("port {} not a valid port".format(port))
            quit()
    sender_in_port = int(args[1])
    sender_out_port = int(args[2])
    chan_send_in_port = int(args[3])
    filename = str(args[4])

    #Checking if input file exists
    if os.path.isfile(filename):
        #Open File in byte mode
        input_file = open(filename, 'rb')
        stdin_successful = True
    else:
        print('File does not exists')

else:
    print("INPUT ERROR. Ports or File invalid")

#if stdin inputs are corerct begin socket initialisation
if stdin_successful:

    print("IN PORT: {}\nOUT PORT: {}\CHAN SENDER IN PORT: {}\nFILENAME: {}"\
    .format(sender_in_port, sender_out_port, chan_send_in_port, filename))


    #Create the sockets
    try:
        sender_in_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(str(e))
    try:
        sender_out_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print(str(e))

    #Bind the sockets
    try:
        sender_in_socket.bind((HOST,sender_in_port))
    except socket.error as e:
        print(str(e))
    try:
        sender_out_socket.bind((HOST,sender_out_port))
    except socket.error as e:
        print(str(e))

    #Connect the sockets
    try:
        sender_out_socket.connect((HOST,chan_send_in_port))
    except socket.error as e:
        print(str(e))


def config_parser():
    """Main Parser function that will check config files are correct """
    pass
