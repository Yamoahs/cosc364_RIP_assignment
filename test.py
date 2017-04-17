import sys
import os.path
import re
import parser
import connection

# Get the arguments list
args = (sys.argv)
# while True:
print("hello")
param = parser.get_params(args)

router = connection.Router_connection(param)

# router.display_router_config()
print(router.in_sockets())
