import socket 
import struct 
import sys

def recv () :
    MCAST_GRP = '224.3.29.71'
    SERVER_ADDR = ('' , 12000 )

    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

    sock.bind(SERVER_ADDR)

    group = socket.inet_aton(MCAST_GRP)
    mreq = struct.pack ('4sL',group,socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP , socket.IP_ADD_MEMBERSHIP , mreq)

    while True :
        print >>sys.stderr, '\nwaiting to receive message'
        data, address = sock.recvfrom(1024)
        
        print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
        print >>sys.stderr, data

        print >>sys.stderr, 'sending acknowledgement to', address
        sock.sendto('I recieved UR', address)

if __name__ == recv():
    recv()