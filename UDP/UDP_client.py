import socket 
import sys
def usage():
    print ("INVALID usage of " + sys.argv[0] + " arguments required as uptime hostnamectl \n")
    print ("Examples : python3 UDP_client.py uptime hostnamectl 'cat /etc/resolv.conf' 'ls -al' 'pwd'")

Total_ARGS = len(sys.argv)
if ( Total_ARGS <= 1) :
    usage()
    exit(-1)
print("Commands to be executed are as follows") 
for arg_num in range(1, Total_ARGS):
    print( (str)(arg_num) + " .) " + sys.argv[arg_num] + " ")

confirm = input ("Type y/Y if above commands are correct : ")
if ( confirm.lower() != 'y') :
    usage()
    exit(-1)

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("\nGOING for SERVER \n")
try:
    for arg_num in range(1, Total_ARGS):
        print("COMMAND PASSED : " + sys.argv[arg_num] + " ") 
        msg = sys.argv[arg_num]
        client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',12345))
        data , addr = client_socket.recvfrom(4096)
        print("\nSERVER RESPONSE")
        print(str(data.decode('utf-8')))
except KeyboardInterrupt:
    print("Exited by user")
print("Executed all commands")
client_socket.close()