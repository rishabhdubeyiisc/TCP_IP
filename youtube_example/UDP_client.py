#!/usr/bin/env python3
import socket 

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg="hello UDP Server"

client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',12345))

data , addr = client_socket.recvfrom(4096)
print("SERVER says")
print(str(data.decode("utf-8")))
client_socket.close()