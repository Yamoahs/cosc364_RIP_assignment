import socket
import time

HOST = "127.0.0.1"
data = "test123"
PORT = 2025

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST,PORT))

while True:
    data = s.recv(1024)
    print(data.decode('utf-8'))
# router-id 1
# input-ports 1025, 1026, 1027
# output-ports 2025-1-2, 6026-5-6, 7025-8-7
