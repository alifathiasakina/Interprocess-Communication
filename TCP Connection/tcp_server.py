import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "127.0.0.1" 
Port = 35821
serv.bind((IP, Port))
pesan = "Socket bind ke alamat " + IP + " dan Port " + str(Port)
print (pesan)
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print (from_client)
        conn.send("I am SERVER\n")
    conn.close()
    print ('client disconnected')