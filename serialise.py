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

# def unpack(data):
#     """Data Loader"""
#     unpacked_data = json.loads(data.decode('utf-8'))
#     return unpacked_data

def unpack(serial):
    """Unpack a serialised routing table string"""
    # 1:2,4|5,7|8,10 (Serialised data format)
    try:
        sentfrm_router_id, routes = serial.split(":")
        routes = routes.strip("\n").split("|")
        rcvd_routes = []
        for route in routes:
            dest, cost, nxt_hop = tuple(route.split(","))
            rcvd_routes.append((dest, cost, nxt_hop))
        return sentfrm_router_id, rcvd_routes
    except:
        return None

def convert(data):
    for node in data:
        data[int(node)] = data.pop(node)
        return data

# r = {1: [1, 0, 1], 4: [4, 0, 4]}
# print(convert(r))
