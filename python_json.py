"""
Python open file Operation

Fungsi untuk bekerja dengan file python adalah menggunakan menggunakan fungsi open()
fungsi open() menggunakan paramater yaitu open("namafile","operasi")

a = append membuka file untuk menambah,membuat baru apabila tidak ada
r = read membuka file untuk dibaca
w = write membuka file untuk menulis
x = create

sebagai tambahan file bisa di handle menggunakan biner atau mode teks

t = Text
b = Binary

"""
import json

file = open("bio.json","r")
load = json.load(file)
print(load["nama"])

# Import Python dictionary to python

data = {
    "nama" : "Asep Supriyatna",
    "umur" : 31,
    "pekerjaan" : "Web Developer"
}

save = json.dumps(data)
print(save)