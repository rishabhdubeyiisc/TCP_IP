#!/usr/bin/env python
import socket 
import struct 

def send() :
    intf = socket.gethostbyname(socket.gethostname())
    MCAST_GRP = "127.0.0.1"
    MCAST_PORT = 12000 

    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM , socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP , socket.IP_MULTICAST_LOOP , 1)
    sock.setsockopt(socket.IPPROTO_IP , socket.IP_MULTICAST_IF, socket.inet_aton(intf))
    message=bytes(("Hello ALL").encode('utf-8'))
    sock.sendto(message, (MCAST_GRP, MCAST_PORT))


if __name__ == '__main__':
    send()
