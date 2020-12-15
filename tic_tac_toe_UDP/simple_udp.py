#!/usr/bin/env python3
import socket 
import sys
import os
import debugger_class
def run_cmd (string):
   stream = os.popen(string)
   read = stream.read()
   print(read)
debug_client = debugger_class.debugger_class(use_debugger=False,verbose_control=False,create_dir=False,filename="client.log")
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr = sys.argv[1]
port = 12345
client_socket.settimeout(0.2)
debug_client.log(debug_client.function_name(),"sending to : " + server_addr )
debug_client.log(debug_client.function_name()," sending to port : "  + str(port))
#msg="      __ GAME __ " + "      Rishabh : X" + "      Surabhi : O" + "      0    1    2" +  "  0 ['-', '-', '-']" + "  1 ['-', 'X', '-']" + "  2 ['-', '-', '-']" + "                      \n"+ "Surabhi enter coordinates"+ ">aa"+ "ERR : INPUT 'length < 2' OR invalid charcters must belong to (0,1,2)"
msg = "hello"
while (True):
    #send
    debug_client.log("While","start")
    debug_client.log("While","send_to begin")
    debug_client.log("While","message sending : " + msg)
    client_socket.sendto(msg.encode("utf-8"),(server_addr,port))
    debug_client.log("While","send_to end")
    #recv
    debug_client.log("While","recvfrom begin")
    data , addr = client_socket.recvfrom(4096)
    debug_client.log("While","addr recieved from : " + str(addr[0]) )
    debug_client.log("While","data recieved from : " + str(data) )
    debug_client.log("While","recvfrom end")
    data = data.decode("utf-8")
    debug_client.log("While","decoded data ")
    print(data)
    #take input
    msg = input('client >')
    debug_client.log("While","user input : " + msg)
    #Exit strategy
    if (msg == "q!"):
        msg = "done_with_game"
        debug_client.log("While","start")
        debug_client.log("While","send_to begin")
        debug_client.log("While","message sending : " + msg)
        client_socket.sendto(msg.encode("utf-8"),(server_addr,port))
        debug_client.log("While","send_to end")
        break
    
client_socket.close()