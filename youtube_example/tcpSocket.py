import socket
import sys

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create a socket")
    print("Reason : %s " + str(err))
    sys.exit()
print('socket created')

target_host=input("Enter the target_host name to connect : ")
target_port=input("Enter the target_port : ")

try:
    sock.connect((target_host,(int(target_port))))
    print("socket connected to %s on port: %s " %(target_host ,target_port ))
    sock.shutdown(2)
except socket.error as err:
    print("Failed to connect to %s on port %s " %(target_host ,target_port ))
    print("Reason : %s " %str(err))
    sys.exit()
