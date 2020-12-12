#! /usr/bin/env pyhton3
import binascii
import socket
import struct
def main ():
    intf = socket.gethostbyname(socket.gethostname())
    host = socket.gethostbyname(socket.gethostname())
    MCAST_GRP = "127.0.0.1"
    MCAST_PORT = 12000 

    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM , socket.IPPROTO_UDP)

    try :
        sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    except AttributeError :
        pass 
    
    sock.setsockopt(socket.IPPROTO_IP , socket.IP_MULTICAST_LOOP , 1)
    
    sock.bind((MCAST_GRP , MCAST_PORT))

    mreq = struct.pack("=4sl", socket.inet_aton(intf), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    
    while True : 
        try :
            data , addr = sock.recvfrom(1024)
            print ("DATA RECV : " + data)
        except socket.error as e :
            print ("EXCEPTION")
            hexdata = binascii.hexlify(data)
            print ('Data = %s' % hexdata)

if __name__ == '__main__':
  main()