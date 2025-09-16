import socket
import datetime
HOST = '127.0.0.1' 
PORT = 60000    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
             data = conn.recv(1024)
            
            #ساعت
             if data =='time':
               conn.sendall(datetime.datetime.now().strftime("%H:%M:%S")) 
             #تاریخ
             else: 
                conn.sendall(datetime.datetime.now().strftime("%Y-%m-%d"))             
                