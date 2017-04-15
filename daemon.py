################################################################################
# File: daemon.py
# Author: sy, jl
# Date created: 15/04/17
# Date Modified: 15/04/17
################################################################################
import sys
import os.path
import re
# import parser

################################################################################
## Global variables
################################################################################
#IP address
HOST =  "127.0.0.1"

# Get the arguments list
args = (sys.argv)

#### /END OF GLOBAL VARIABLES
################################################################################

def load_file(args):
    #Flag for succesful load of config file
    load_successful = False

    #Valid File Format
    CONFIG_PATTERN = re.compile("router[0-9]+_config")

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

    return config_file, load_successful


def info_check(config_file, load_successful):
    config_info = []

    #Flag for valid config file
    config_successful = True

    #Flag for valid customer timer parameter
    valid_timer = None

    for line in config_file:
        #Filters out blank lines and comments. Comments start with "#"
        if not re.search(r'^\s|^#.*', line):
            config_info.append(line.split())
    # print(config_info)

    if 3 < len(config_info) < 4:
        print("CONFIG ERROR: Router is missing or containing extra parameters")
        quit()
    else:
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
            print(config_info[3], 'len:', len(config_info[3]))
            if (len(config_info[3]) != 2) or config_info[3][0] != "timer":
                config_successful = False
                print("TIMER ERROR")
                quit()
            else:
                valid_timer = True

    return config_info, config_successful, valid_timer


def set_params(config_info, config_successful, valid_timer):
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
        if  valid_timer:
            timer = config_info[3][1]
            return(router_id, input_ports, output_ports, timer)

        else:
            timer = None
            return(router_id, input_ports, output_ports, timer)


config_file, load_successful = load_file(args)
config_info, config_successful, valid_timer = info_check(config_file, load_successful)
parameters = set_params(config_info, config_successful, valid_timer)
print(parameters)
