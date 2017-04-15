################################################################################
# File: parser.py
# Author: sy, jl
# Date created: 27/03/17
# Date Modified: 3/04/17
################################################################################
import sys
import os.path
import re

################################################################################
## Global variables
################################################################################

#IP address
HOST =  "127.0.0.1"

#valid Port no.
VALID_PORTS =  range(1024, 64001)

# Get the arguments list
args = (sys.argv)

#Flag for succesful load of config file
load_successful = False

#Flag for valid config file
config_successful = True

#Flag for valid customer timer parameter
custom_timer = False
valid_timer = False

#Valid File Format
CONFIG_PATTERN = re.compile("router[0-9]+_config")

#### /END OF GLOBAL VARIABLES

def print_config(router_id, input_ports, output_ports, timer = None):
    print("Router ID: ", router_id)
    print("Input Ports: ", input_ports)
    print("Output Ports: ", output_ports)
    if valid_timer:
        print("timer: ", timer)
##END OF FUNCTION

################################################################################
## First check to make sure a valid config file is supplied
################################################################################

if len(args) == 2:
    filename = args[1]
    path = "./config_files/" + filename
    if not CONFIG_PATTERN.match(filename):
        print("FILE ERROR: File not a valid Configuration format")
        quit()
    else:
        #Check if config file exists
        if os.path.isfile(path):
            print("whoop whoop")
            #Open File in normal mode
            config_file = open(path, 'r')
            load_successful = True
        else:
            print("FILE ERROR: File does not exist")
            quit()
else:
     print("INPUT ERROR: No Router Config file specified")
     quit()

################################################################################

#TODO Do we want to check each file to make sure it has the 3 fields? (id, in/out)
##FUNCTION
if load_successful:
    config_info = []
    for line in config_file:
        #Filters out blank lines and comments. Comments start with "#"
        if not re.search(r'^\s|^#.*', line):
            config_info.append(line.split())
    # print(config_info)

    ##collect the router ID
    if config_info[0][0] != "router-id" and len(config_info[0]) != 2:
        config_successful = False
        print("ROUTER-ID ERROR")
        quit()

    if config_info[1][0] != "input-ports" and len(config_info[1]) < 2:
        config_successful = False
        print("INPUT-PORT(S) ERROR")
        quit()

    if config_info[2][0] != "output-ports" and len(config_info[2]) < 2:
        config_successful = False
        print("INPUT-PORT(S) ERROR")
        quit()


    ##Check if timer values have been specified in the config file
    if len(config_info) == 4:
        custom_timer = True
        if config_info[3][0] != "timer" and len(config_info[3]) != 2:
            config_successful = False
            print("TIMER ERROR")
            quit()
        else:
            valid_timer = True

##Set all the variables
if config_successful:
    #Router ID
    router_id = config_info[0][1]

    ##loop through the input Ports
    input_ports = []
    for port_numbr in config_info[1][1:]:
        if port_numbr[-1] == ",":
            port_numbr = port_numbr[:-1]
        input_ports.append(int(port_numbr))

    ##loop through the output config_info
    output_ports = []
    for port_numbr in config_info[2][1:]:
        if port_numbr[-1] == ",":
            port_numbr = port_numbr[:-1]
        output_ports.append(port_numbr.split("-"))
    for output in range(len(output_ports)):
        output_ports[output] = list(map(int, output_ports[output]))

    #Set timer if timer parameters have been provided
    if custom_timer and valid_timer:
        timer = config_info[3][1]
        print_config(router_id, input_ports, output_ports, timer)

    else:
        print_config(router_id, input_ports, output_ports)




#closing the file
config_file.close()



def config_parser():
    """Main Parser function that will check config files are correct """
    pass
