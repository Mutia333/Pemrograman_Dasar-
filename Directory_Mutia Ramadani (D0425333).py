#Nama : [Mutia Ramadani]
#NIM : [D0425333]
#Materi : Dictionary

data_buku = {
    "judul": "Belajar Python",
    "penulis": "Mutia",
}

#menambah data
data_buku["tahun"] = 2025
#menghapus data
del data_buku["penulis"]
#mengubah data
data_buku["judul"] = "Pemrograman Python Dasar"
#percabangan
if "penerbit" in data_buku:
    print("Data lengkap")
else:
    print("Data tidak lengkap")
#menghitung data
print(len(data_buku))
print(data_buku)
