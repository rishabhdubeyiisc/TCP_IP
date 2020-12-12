import socket 

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#hostnamectl
#uptime
#cat /etc/resolv.conf
msg='hostnamectl'

try:
    while (True):
        client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',12345))
        data , addr = client_socket.recvfrom(4096)
        print("SERVER says")
        print(str(data.decode('utf-8')))
        more = input('Want to send more data to server ??')
        if more.lower() == 'y' :
            msg = input ("Enter payload")
        else:
            break
except KeyboardInterrupt:
    print("Exited by user")

client_socket.close()