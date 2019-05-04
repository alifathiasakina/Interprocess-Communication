# import library socket karena menggunakan IPC socket
import socket

# definisikan IP untuk binding
IP = "127.0.0.1"

# definisikan port untuk binding
Port = 14000

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

# buka/buat file bernama hasil_upload.txt untuk menyimpan hasil dari file yang dikirim server
# masih hardcoded nama file, bertipe byte
f = open('hasil_upload.txt','wb')


# loop forever
while 1:
    # terima pesan dari client
    data = conn.recv(Buffer)
    
    # tulis pesan yang diterima dari client ke file kita (result.txt)
    while (data):
        print ("Receiving...")
        f.write(data)
        data = conn.recv(1024)
       
    
    # berhenti jika sudah tidak ada pesan yang dikirim
    
    
# tutup file result.txt    
    f.close()

#tutup socket
s.close()          

# tutup koneksi
conn.close()