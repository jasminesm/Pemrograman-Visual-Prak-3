#Nama  : Jasmine Sarah Maqnolia
#Nim   : 20051397078
#Kelas : 2020B
#Prodi : Manajemen Informatika


def cekpalindrom (teks) :
    list = []
    belakang = ''
    depan = ''
    indikator = True
    for i in range (len(teks)) :
        if teks[i] != ',' and teks[i] != '.' and teks[i] != "'" and teks[i] != '"' and teks[i] != '!' and teks[i] != '?' and teks[i] != ' ' :
            list.append(teks[i])
    while len(list) > 1 and indikator  :
        depan += list.pop(0)
        belakang += list.pop()
        if belakang != depan :
            indikator = False
    if indikator :
        print(teks, "adalah kata palyndrom.")
    else :
        print(teks, "bukan kata palyndrom.")


a = input('masukkan teks : ')

print('hasil : ')
cekpalindrom (a)