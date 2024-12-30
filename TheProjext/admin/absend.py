from console import db

def administrasi():
    nomor = int(input('Masukan Nomor : '))
    nama = input('Masukan Nama : ')
    gender = input('Masukan Gender : ')

    db.add_members(nomor,nama,gender)

def check():
    check = db.check()
    for i in check:
        id=i[0]
        nomor=i[1]
        nama=i[2]
        gender=i[3]
        print(f'''
ID : {id}
Absend : {nomor}
Nama Lengkap : {nama}
Jenis Kelamin : {gender}
''')

def absend():

    check = db.check()
    for i in check:
        nomor=i[1]
        nama=i[2]
        gender=i[3]

    nomor = int(input('Masukan Nomor : '))
    nama = input('Masukan Nama : ')
    gender = input('Masukan Gender : ')

    if nomor and nama and gender in i:
        print('\nNama Kamu Terverifikasi\n')
    else:
        print('\nGagal verifikasi\n')



def delete():
    ID = int(input('Masukan ID yang akan dihapus = '))

    db.Delete(ID)



def main():
    while True:
        menu = int(input("\nMenu:\n1.Administrasi\n2.Check\n3.Absend\n4.Delete\n# OUT\n\npilih : "))

        if menu == 1:
            administrasi()
        elif menu == 2:
            check()
        elif menu == 3:
            absend()
        elif menu == 4:
            delete()
        elif menu == 0:
            break
        else:
            print('........!')

if __name__ == '__main__':
    main()

