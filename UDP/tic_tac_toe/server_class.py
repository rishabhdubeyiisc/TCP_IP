#!/usr/bin/env python3
import socket 
import sys

class game_server:    
    IPAddr = "127.0.0.1"
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',12345))
    sender_addr = None
    def __init__(self , port = 12345):
        print("Creating network")
        self.get_ipv4()
        print("ipv4 : " + self.IPAddr)
        sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind((self.IPAddr,port))

    def get_ipv4(self):
        hostname = socket.gethostname()    
        self.IPAddr = socket.gethostbyname(hostname)

    def recv_data(self):
        in_string , self.sender_addr = self.sock.recvfrom(4096)
        in_string = in_string.decode("utf-8")
        return in_string
    
    def send_ack (self , string):
        message=bytes((string).encode("utf-8"))
        self.sock.sendto(message,self.sender_addr)

"""
if __name__ == "__main__":
    server = game_server()
    while (True):
        incoming_string = server.recv_data()
        print(incoming_string)
        server.send_ack("hi from")   
"""
"""
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = sys.argv[1]
sock.bind((addr,12345))

while (True):
    data , addr = sock.recvfrom(4096)
    print(str(data.decode("utf-8")))
"""