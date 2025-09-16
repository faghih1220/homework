import socket  
with socket.socket (socket.AF_INET,socket.SOCK_STREAM) as s:
     s.connect(("127.0.0.1",60000))
#s.bind((HOST, PORT))
     s.listen()
     conn, addr = s.accept()
     with conn:
          while True:
              s.sendall("hello")
              data = s.recv(1024)
              s.sendall(data)