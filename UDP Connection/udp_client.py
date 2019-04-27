# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju
IP_DST = "127.0.0.1"

# definisikan target port number server yang akan dituju
PORT_DST = 54321
Message = "Hai Alif!"
print ("IP target:", IP_DST)
print ("Port target:", PORT_DST)
print ("Pesan:", Message)

# buat socket bertipe UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# lakukan loop 10 kali
for x in range (10):
    # kirim pesan
    s.sendto(Message.encode(),(IP_DST,PORT_DST))