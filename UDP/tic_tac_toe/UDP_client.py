#!/usr/bin/env python3
import socket 
import sys
try:
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except socket.error as err :
    exit (-1)
try:
    addr = sys.argv[1]
    for arg_num in range(2, len(sys.argv)):
        print("COMMAND PASSED : " + sys.argv[arg_num] + " ") 
        msg = sys.argv[arg_num]
        print ("msg : " + msg + " to addr : " + addr)
        print (type(msg) , type(addr) )
        client_socket.sendto(msg.encode("utf-8"),(addr,12345))
        data , addr = client_socket.recvfrom(4096)
        print("\nSERVER RESPONSE")
        print(str(data.decode('utf-8')))
except KeyboardInterrupt:
    print("Exited by user")
finally :
    print("Executed all commands")
client_socket.close()