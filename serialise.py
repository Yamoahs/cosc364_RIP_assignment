################################################################################
# File: serialise.py
# Author: sy, jl
# Date created: 15/04/17
# Date Modified: 04/05/17
################################################################################
import json
import socket

def pack(data):
    """Data Serialised"""
    packed_data = json.dumps(data).encode('utf-8')
    return packed_data

def unpack(data):
    """Data Loader"""
    unpacked_data = json.loads(data.decode('utf-8'))
    return unpacked_data

def convert(data):
    for node in data:
        data[int(node)] = data.pop(node)
        return data

# recieved data:  [{1: [1, 0, 1]}, {4: [4, 0, 4]}]
