import socket 
with socket.socket (socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1",60000))
    list=['مشهد بارانی دما 10 درجه','تهران الوده دما20 درجه','مازندران مه الود دما 5درجه']
    for i in list:
        s.sendall(i.encode())
        data=s.recv(1024)
        print(data.decode())
        if data==list:
          s.sendall(print(list))
        else:
           s.sendall(print("اب و هوای این شهر هنوز  اعلام نشده است"))