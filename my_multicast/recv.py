import socket 
import struct 
import sys
import select
def add_socket_to_group (sock , group ):
    membership_request = struct.pack ('4sL',group,socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP , socket.IP_ADD_MEMBERSHIP , membership_request)

def drop_socket_from_group (sock , multicast_ip , group ):
    membership_request = struct.pack ('4sL',group,socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, membership_request)

def recv () :
    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    SERVER_ADDR = ('' , 12000 )
    sock.bind(SERVER_ADDR)
    #create group
    MCAST_GRP = '224.3.29.71'
    mcast_group = socket.inet_aton(MCAST_GRP)
    #add to group
    add_socket_to_group( sock , mcast_group )
    #drop from group

    while True :
        ADDR = (MCAST_GRP , 12000)
        readers , _, _ = select.select([sys.stdin , sock] , [] , [])
        for reader in readers :
            if reader is sock :        
                #print("Wait on recv")
                data, address = sock.recvfrom(4096)
                ADDR = address
                print ( "recieved " + str(len(data)) + " bytes  " + " from " + str(address) )
                print ( "\n data came as : " + data.decode("utf-8") )
            else :
                msg = input ('> ')
                #print ('sending acknowledgement to' + str(address) )
                # msg = "ACK from recv"
                # sock.sendto( msg.encode("utf-8"), ADDR)

if __name__ == recv():
    recv()