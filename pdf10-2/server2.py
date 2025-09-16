import socket
HOST = '127.0.0.1' 
PORT = 60000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            s.sendall(b"Hi ")
            data = s.recv(1024)
            conn .sendall(s)
    