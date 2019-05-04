# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
IP = "127.0.0.1"

# definisikan port untuk binding
Port = 15000

# definisikan ukuran buffer untuk menerima pesan
Buffer = 4096

# buat socket (bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan binding ke IP dan port
s.bind((IP,Port))

# lakukan listen
s.listen(1)
print("Is listening")

#  siap menerima koneksi
conn,addr = s.accept()

print ('Connection address:', addr)
print("downloading")

# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte
f = open('file_didownload.txt','rb')

try:
   
    # baca file tersebut sebesar buffer 
    l = f.read(4096)
    
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while (l):
        # kirim hasil pembacaan file
        conn.send(l)
        
        # baca sisa file hingga EOF
        l = f.read(4096)
        #print(byte)
finally:
    print ("end sending")
    
    # tutup file jika semua file telah  dibaca
    f.close()
    

# tutup socket
s.close()

# tutup koneksi
conn.close()