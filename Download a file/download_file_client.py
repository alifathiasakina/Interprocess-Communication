# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
IP_DST = "127.0.0.1"

# definisikan port number proses di server
PORT_DST = 15000

# definisikan ukuran buffer untuk mengirim
BUFFER_SIZE = 4096

# buat socket (apakah bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server
s.connect((IP_DST, PORT_DST))


# buka file bernama "hasil_download.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open('hasil_download.txt', 'wb')
print("Sending...")

# loop forever
while 1:
    # terima pesan dari client
    data=s.recv(BUFFER_SIZE)
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    while (data):
        print ("Downloading...")
        f.write(data)
        data = s.recv(4096)
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    if not data: break
    
# tutup file_hasil_download.txt    
    f.close()

#tutup socket
s.close()
