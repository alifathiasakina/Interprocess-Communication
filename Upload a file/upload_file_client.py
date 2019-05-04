# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload
IP_DST = "127.0.0.1"

# definisikan port number proses di server
PORT_DST = 14000

# definisikan ukuran buffer untuk mengirim
BUFFER_SIZE = 4096

# buat socket (apakah bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan koneksi ke server
s.connect((IP_DST, PORT_DST))

# buka file bernama "file_diupload.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python
f = open('file_diupload.txt', 'rb')
print("Sending...")


try:
    # baca file tersebut sebesar buffer 
    l = f.read(4096)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while (l):
        # kirim hasil pembacaan file
        s.send(l)
        
        # baca sisa file hingga EOF
        l = f.read(4096)
        #print(byte)
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()

# tutup koneksi setelah file terkirim
s.close()