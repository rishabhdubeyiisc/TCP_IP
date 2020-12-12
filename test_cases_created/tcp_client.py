import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',12345))

payload='hey Server'

try:
    while (True):    
        client_socket.send(payload.encode('utf-8'))
        #buffer size
        data = client_socket.recv(1024)
        print(str(data))
        more = input('Want to send more data to server')
        if more.lower() == 'y':
            payload=input("Enter Payload")
        else:
            break
except KeyboardInterrupt :
    print("Exited by User")

client_socket.close()