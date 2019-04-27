# import library socket karena akan menggunakan IPC socket
import socket

# definisikan tujuan IP server
IP_DST = "127.0.0.1"

# definisikan port dari server yang akan terhubung
PORT_DST = 54321

# definisikan ukuran buffer untuk mengirimkan pesan
BUFFER_SIZE = 1024

# definisikan pesan yang akan disampaikan
Message ="Hai lagi, Alif!"

# buat socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((IP_DST, PORT_DST))

# kirim pesan ke server
s.send(Message.encode())

# terima pesan dari server
data = s.recv(BUFFER_SIZE)

# tampilkan pesan/reply dari server
print ("Received data:", data.decode())

# tutup koneksi
s.close()

