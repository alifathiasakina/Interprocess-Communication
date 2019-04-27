import socket

UDP_IP = "127.0.0.1"
UDP_Port = 35821

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((UDP_IP, UDP_Port))

while True:
    data, addr  = sock.recvfrom(4096)
    print(addr)
    print("Pesan diterima", data.decode())