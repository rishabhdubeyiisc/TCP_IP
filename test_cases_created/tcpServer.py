import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1',12345))
#% here means that 5 connection will wait if server is busy
server_socket.listen(5)

while (True):
    print("Server Waiting for connection")
    client_socket,addr=server_socket.accept()
    print("Client connected from :" , addr)
    while (True) :
        #1024 for bytes input
        data=client_socket.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break
        print ("recieved from client : %s " % data.decode("utf-8"))
        try:
            client_socket.send(bytes('Hey client','utf-8'))
        except:
            print("Exited by the user")
    client_socket.close()
