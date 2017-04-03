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
config_successful = False

#Valid File Format
PATTERN = re.compile("router[0-9]+_config")

#### /END OF GLOBAL VARIABLES


################################################################################
## First check to make sure a valid config file is supplied
################################################################################

if len(args) == 2:
    filename = args[1]
    path = "./config_files/" + filename
    if not PATTERN.match(filename):
        print("FILE ERROR: File not a valid Configuration format")
        quit()
    else:
        #Check if config file exists
        if os.path.isfile(path):
            print("whoop whoop")
            #Open File in normal mode
            config_file = open(path, 'r')
            config_successful = True
        else:
            print("FILE ERROR: File does not exist")
            quit()
else:
     print("INPUT ERROR: No Router Config file specified")
     quit()

#TODO Do we want to check each file to make sure it has the 3 fields? (id, in/out)
##FUNCTION
if config_successful:
    info = []
    for line in config_file:
        info.append(line.split())
    print(info)
for i in info[2]:
    print(i)

##END OF FUNCTION


#closing the file
config_file.close()



def config_parser():
    """Main Parser function that will check config files are correct """
    pass
