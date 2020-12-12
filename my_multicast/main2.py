#! /usr/bin/python3
import socket 
import struct 
import sys
import time
import select
def usage () :
    print ("pass arguments as -s == sender , -r == reciever , -v == verbose")

def add_socket_to_group (sock , group ):
    membership_request = struct.pack ('4sL',group,socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP , socket.IP_ADD_MEMBERSHIP , membership_request)

def drop_socket_from_group (sock , multicast_ip , group ):
    membership_request = struct.pack ('4sL',group,socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, membership_request)

def recv (verbose) :
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
        ADDR_COPY = (MCAST_GRP , 12000)
        readers , _, _ = select.select([sys.stdin , sock] , [] , [])
        for reader in readers :
            if reader is sock :        
                data, address = sock.recvfrom(4096)
                ADDR_COPY = address
                print ( "recieved " + str(len(data)) + " bytes  " + " from " + str(address) )
                print ( "\n data came as : " + data.decode("utf-8") )
            else :
                msg = input ('> ')
                if (verbose == True) :
                    print ("User input : " + msg)

def create_group_and_send(MCAST_GRP) :
    MCAST_GRP = ('224.3.29.71' , 12000)
    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    sock.settimeout(0.2)

    ttl = struct.pack('b' , 1)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.INADDR_ANY)

    print ("Created a Group @ : " + str(MCAST_GRP[0]) + " Port : " + str (MCAST_GRP[1])) 

    message = "This is Multicast Group"
    try :
        while True :
            print ("Sending msg :" + message)
            #print("Wait on recv")
            # try :
            #send the msg
            sent = sock.sendto(message.encode("utf-8") , MCAST_GRP)
            val = input('Want to send more data to server(Y/n) : ')
            if (val.lower() == 'y'):
                message=input("Enter Payload                         : ")
            else:
                break
            try :
                #recieve the msg from reciever
                data , server = sock.recvfrom(4096)
                print ("recieved : " + str(data.decode("utf-8")) + " from : " + str(server))
            except socket.timeout :
                #print ("ERR : TIMEOUT No data coming from reciever ")
                pass                
    finally :
        print("Closing Socket")
        sock.close()

if __name__ == '__main__' :
    MCAST_GRP = ('224.3.29.71' , 12000)
    verbose = False
    if (len(sys.argv) > 2 and sys.argv[2] == "-v") :
        verbose = True
    if sys.argv[1] == "-s" :
        create_group_and_send(MCAST_GRP)
    elif sys.argv[1] == "-r" :
        recv(verbose) 
    else:
        usage()