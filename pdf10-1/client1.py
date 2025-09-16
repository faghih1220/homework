import socket
import time  
with socket.socket (socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1",60000))
    list=['time','data']
    for i in list:
        s.sendall(i.encode())
        data=s.recv(1024)
        print(data.decode())
