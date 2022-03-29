#Nama  : Jasmine Sarah Maqnolia
#Nim   : 20051397078
#Kelas : 2020B
#Prodi : Manajemen Informatika


def pembalik(teks) :
    list = []
    hasil = ''
    for i in range (len (teks)) :
        list.append(teks[i])
    while list != [] :
        hasil += list.pop()
    return hasil
a = input("masukkan teks : ")
print("Hasil : " , pembalik (a))