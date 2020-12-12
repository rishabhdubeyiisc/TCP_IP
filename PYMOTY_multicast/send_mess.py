import socket 
import struct 
import sys

def send() :
    message = "very imp data"

    MCAST_GRP = ('224.3.29.71' , 12000)
    sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

    sock.settimeout(0.2)

    ttl = struct.pack('b' , 1)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    try :
        #print (>>sys.stderr, 'sending "%s"' % message)
        print ("Sending msg :" + message)
        # client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',12345))

        while True :
            # print >>sys.stderr, 'waiting to receive'
            print("Wait on recv")
            try :
                #mention buffer
                sent = sock.sendto(message.encode("utf-8") , MCAST_GRP)
                data , server = sock.recvfrom(100)
                #print >>sys.stderr, 'received "%s" from %s' % (data, server)
                print ("recieved : " + str(data) + " from : " + str(server))
                val = input('Want to send more data to server(Y/n) : ')
                if (val.lower() == 'y'):
                    message=input("Enter Payload : ")
                else:
                    break
            except socket.timeout :
                #print >> sys.stderr , 'time out, no more response'
                print ("Timeout error")
                break                
    finally :
        #print >>sys.stderr, 'closing socket'
        print("Closing Socket")
        sock.close()

if __name__ == send() :
    send()