#!/usr/bin/env python3
import socket 
import sys
import os
def run_cmd (string):
   stream = os.popen(string)
   read = stream.read()
   print(read)

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr = sys.argv[1]
#msg="      __ GAME __ " + "      Rishabh : X" + "      Surabhi : O" + "      0    1    2" +  "  0 ['-', '-', '-']" + "  1 ['-', 'X', '-']" + "  2 ['-', '-', '-']" + "                      \n"+ "Surabhi enter coordinates"+ ">aa"+ "ERR : INPUT 'length < 2' OR invalid charcters must belong to (0,1,2)"
msg = "hello"
while (True):
    client_socket.sendto(msg.encode("utf-8"),(server_addr,12345))
    data , addr = client_socket.recvfrom(4096)  
    data = data.decode("utf-8")
    print(data)
    msg = input('>')
client_socket.close()