import socket
from _thread import *

server_socket= socket.socket()

host="127.0.0.1"
port=12345

thread_count=0

try:
    server_socket.bind((host,port))
except socket.error as err :
    print(str(err))
print("waiting for connection")

server_socket.listen()

def client_thread(connection):
    connection.send(str.encode("welcome to the server"))
    while (True):
        data=connection.recv(2048)
        reply="Hello Im server" + data.decode("utf-8")
        if not data :
            break 
        connection.sendall(str.encode(reply))
    connection.close()

while(True):
    client,addr = server_socket.accept()
    print("connected to " + addr[0] + " " + str(addr[1]))
    start_new_thread(client_thread,(client,))
    thread_count+=1
    print("Threadnumber " + str(thread_count))
server_socket.close()