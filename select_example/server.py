import socket 

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))

while (True):
    data , addr = sock.recvfrom(4096)
    print(str(data.decode("utf-8")))
    message=input('> ')
    sock.sendto(message.encode("utf-8") ,addr)

