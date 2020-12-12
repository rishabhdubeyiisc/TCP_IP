import socket 
import select
import sys
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('127.0.0.1',12345))
while True :
    readers , _, _ = select.select([sys.stdin , s] , [] , [])
    for reader in readers :
        #if socket buf hits we go in if or we go in else 
        if reader is s :
            data , addr = s.recvfrom(4096)
            print ("< " + str(data.decode("utf-8")))
        else :
            msg = input ('> ')
            s.sendto(msg.encode("utf-8"),('127.0.0.1',12345))
            
