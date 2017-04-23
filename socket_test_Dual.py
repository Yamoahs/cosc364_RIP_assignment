import socket
import select
import time
import sys
import os.path

# Get the arguments list
args = (sys.argv)

HOST = "127.0.0.1"
data = "Hello from router {}".format(args[1])
PORTA = 2025
PORTB = 2026


inputt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
output = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind input on either end to listen
inputt.bind((HOST, PORTA))
output.bind((HOST, PORTB))

def send_data(socket, data, port):
    socket.sendto(data.encode('utf-8'), (HOST, port))
    print("sent ", data)

def recv_data(socket):
    available = select.select(socket, [], [], 0.1) # wait for 100ms, only interested in reading
    data = socket.recv(1024)
    print(data.decode('utf-8'))



while True:
    if args[1] == 1:
        send_data(output, data, PORTA)
    else:
        send_data(output, data, PORTB)
    time.sleep(1)
    if args[1] == 2:
        recv_data(inputt)
    else:
        recv_data(output)
# router-id 1
# input-ports 1025, 1026, 1027
# output-ports 2025-1-2, 6026-5-6, 7025-8-7
