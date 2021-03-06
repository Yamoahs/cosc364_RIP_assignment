################################################################################
# File: parser.py
# Author: sy, jl
# Date created: 27/03/17
# Date Modified: 16/04/17
################################################################################
import sys
import os.path
import re


def load_file(args):
    #Flag for succesful load of config file
    load_successful = False

    #Valid File Format
    CONFIG_PATTERN = re.compile("router[0-9]+_config")

    if len(args) == 2:
        filename = args[1]
        path = "./config_files/" + filename + ".cfg"
        if not CONFIG_PATTERN.match(filename):
            print("FILE ERROR: File not a valid Configuration format")
            quit()
        else:
            #Check if config file exists
            if os.path.isfile(path):
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

    #Flag for valid customer update timer parameter
    valid_update_timer = None
    #Flag for valid customer timeout timer parameter
    valid_timeout_timer = None
    #Flag for valid customer garbage timer parameter
    valid_garbage_timer = None

    for line in config_file:
        #Filters out blank lines and comments. Comments start with "#"
        if not re.search(r'^\s|^#.*', line):
            config_info.append(line.split())
    # print(config_info)

    if 3 < len(config_info) < 6:
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

        ##Check if update timer values have been specified in the config file
        if len(config_info) == 4:
            print(config_info[3], 'len:', len(config_info[3]))
            if (len(config_info[3]) != 2) or config_info[3][0] != "update":
                config_successful = False
                print("TIMER ERROR: Update")
                quit()
            else:
                valid_update_timer = True

        ##Check if timeout timer values have been specified in the config file
        if len(config_info) == 5:
            # print(config_info[3], 'len:', len(config_info[3]))
            if (len(config_info[4]) != 2) or config_info[4][0] != "timeout":
                config_successful = False
                print("TIMER ERROR: Timeout")
                quit()
            else:
                valid_timeout_timer = True

        ##Check if garbage timer values have been specified in the config file
        if len(config_info) == 6:
            # print(config_info[3], 'len:', len(config_info[3]))
            if (len(config_info[5]) != 2) or config_info[5][0] != "garbage":
                config_successful = False
                print("TIMER ERROR: Timeout")
                quit()
            else:
                valid_garbage_timer = True

    #closing the file
    config_file.close()

    return config_info, config_successful, valid_update_timer,\
                                        valid_timeout_timer, valid_garbage_timer


def set_params(config_info, config_successful,\
                  valid_update_timer, valid_timeout_timer, valid_garbage_timer):
    ##Set all the variables

    #valid Port no.
    VALID_PORTS =  range(1024, 64001)
    if config_successful:
        #Router ID
        router_id = config_info[0][1]

        ##loop through the input Ports
        input_ports = []
        for port_numbr in config_info[1][1:]:
            if port_numbr[-1] == ",":
                port_numbr = port_numbr[:-1]
            if int(port_numbr) not in VALID_PORTS:
                print("PORT ERROR: An In-port number not within vald range")
                quit()
            else:
                input_ports.append(int(port_numbr))

        ##loop through the output config_info
        output_ports = []
        for port_numbr in config_info[2][1:]:
            if port_numbr[-1] == ",":
                port_numbr = port_numbr[:-1]
            output_ports.append(port_numbr.split("-"))
        for output in range(len(output_ports)):
            output_ports[output] = list(map(int, output_ports[output]))
        for port_numbr in output_ports:
            if int(port_numbr[0]) not in VALID_PORTS:
                print("PORT ERROR: an Out-port number not within vald range")
                quit()

        #Set timers if all timer parameters have been provided
        if  valid_update_timer and valid_timeout_timer and valid_garbage_timer:
            update_timer = config_info[3][1]
            timeout_timer = config_info[4][1]
            garbage_timer = config_info[5][1]

            return(router_id, input_ports, output_ports, update_timer,\
                                                   timeout_timer, garbage_timer)

        else:
            update_timer = None
            timeout_timer = None
            garbage_timer = None
            return(router_id, input_ports, output_ports, update_timer,\
                                                   timeout_timer, garbage_timer)


def get_params(args):
    config_file, load_successful = load_file(args)
    config_info, config_successful, valid_update_timer, valid_timeout_timer,\
                  valid_garbage_timer = info_check(config_file, load_successful)
    parameters = set_params(config_info, config_successful, valid_update_timer,\
                                       valid_timeout_timer, valid_garbage_timer)
    return(parameters)
