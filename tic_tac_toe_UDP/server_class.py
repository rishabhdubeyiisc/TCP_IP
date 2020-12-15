#!/usr/bin/env python3
import socket 
import sys
import debugger_class

verbose_control_FILE = True
use_debugger_FILE = True

class game_server:    
    IPAddr = "127.0.0.1"
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sender_addr = None
    port = 12345
    debugger_nw = debugger_class.debugger_class( use_debugger=False, 
                                                 verbose_control = False,
                                                 filename = "server_class.log" )
    def __init__(self , port = 12345 , use_debugger = use_debugger_FILE , verbose_control = verbose_control_FILE , get_IPv4_override = False) :
        self.debugger_nw = debugger_class.debugger_class(create_dir=False ,
                                                         use_debugger=use_debugger_FILE, 
                                                         verbose_control = verbose_control_FILE,
                                                         filename = "game_server.log")
        self.debugger_nw.log("game_server_init","initializing game server Creating network")
        if (get_IPv4_override):
            self.get_ipv4()
        self.port = port
        self.debugger_nw.log("game_server_init IPv4 ", self.IPAddr)
        self.debugger_nw.log("game_server_init PORT ", str(self.port))
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sock.bind((self.IPAddr,port))
        self.debugger_nw.log("game_server_init ","sock.bind try")

    def get_ipv4(self):
        hostname = socket.gethostname()    
        self.IPAddr = socket.gethostbyname(hostname)

    def recv_data(self):
        self.debugger_nw.log("game_server.recv_data","recieving data")
        in_string , self.sender_addr = self.sock.recvfrom(4096)        
        in_string = in_string.decode("utf-8")
        self.debugger_nw.log("game_server.recv_data","recieved data : " + str(in_string) + " from : " + str(self.sender_addr[0]))
        return str(in_string)
    
    def send_ack (self , string):
        self.debugger_nw.log("game_server.send_ack","sending data : " + str(string))
        message=bytes((string).encode("utf-8"))
        self.sock.sendto(message,self.sender_addr)
        self.debugger_nw.log( "game_server.send_ack"," sent data to : " + str(self.sender_addr[0]) )

