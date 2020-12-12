#! /usr/bin/python3
import socket 
import struct 
import sys
import time
import select

def create_group_and_send() :
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
                print ("ERR : TIMEOUT No data coming from reciever ")
                pass                
    finally :
        print("Closing Socket")
        sock.close()

if __name__ == create_group_and_send() :
    create_group_and_send()