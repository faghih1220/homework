import socket 
with socket.socket (socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1",60000))
    
    
    a=input("name city:")
    s.sendall(a)