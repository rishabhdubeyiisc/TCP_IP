#!/usr/bin/env python3
import socket 
import sys
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = sys.argv[1]
msg="11 this is my packet"

client_socket.sendto(msg.encode("utf-8"),(addr,12345))
data , addr = client_socket.recvfrom(4096)
client_socket.close()