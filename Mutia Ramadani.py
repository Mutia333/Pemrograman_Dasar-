#Nama : [Mutia Ramadani]
#NIM : [D0425333]
#Materi : Array

angka = [5, 15, 25, 35]
#menambah data
angka.append(45)
#mengubah data
angka[1] = 20
#menghapus data
del angka[0]
#menghitung jumlah data
print(len(angka))
#percabangan
if 25 in angka:
    print("Angka 25 ada di dalam list")
else:
    print("Angka 25 tidak ada di dalam list")
print(angka)
