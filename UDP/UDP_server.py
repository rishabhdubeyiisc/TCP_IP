import socket 
import os

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('127.0.0.1',12345))

while (True):
    # addr may change easily but have to be stored to sendback easily
    #bytes to accept to cover entire msg
    data , addr = sock.recvfrom(4096) # 4096 bytes
    print(str(data.decode('utf-8')))
    stream = os.popen(str(data.decode('utf-8')))
    read=stream.read()
    message=bytes((read).encode('utf-8'))
    sock.sendto(message,addr)

