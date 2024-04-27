print(('-')*20,'PROGRAM KASIR.PY',('-')*20)

pembeli = input("Masukan Nama Pembeli: ")
print("Nama:",pembeli)

def list_makanan():
    global totalmkn
    global porsi
    global mkn
    print(('-')*20,'Menu Makanan',('-')*20)
    print("1.SOTO AYAM   : 10.500\n"
          "2.MIE AYAM    : 10.500\n"
          "3.PANGSIT      : 6.000\n"
          "4.AYAM GEPREK : 10.OOO")
    print(('-')*40,'\n')
    nomor = int(input("Masukan Pilihan: "))
    porsi = int(input("Masukan Porsi  : "))

    if nomor == 1:
        totalmkn = porsi * 10500
        print("Soto Ayam\t",porsi,'\t',totalmkn)
        mkn = ("Soto Ayam")
    elif nomor == 2:
        totalmkn = porsi * 10500
        print("Mie Ayam\t",porsi,'\t',totalmkn)
        mkn = ("Mie Ayam")
    elif nomor == 3:
        totalmkn = porsi * 6000
        print("Pangsit\t",porsi,'\t',totalmkn)
        mkn = ("Pangsit")
    elif nomor == 4:
        totalmkn = porsi * 10000
        print("Ayam Geprek\t",porsi,'\t',totalmkn)
        mkn = ("Ayam Geprek")
    else:
        print("invalid silahkan pilih yang sesuai di menu")
        list_makanan()

list_makanan()

print("HARGA JUAL : ",totalmkn)
uang = int(input("TUNAI : "))
kembalian = int(uang-totalmkn)
print("KEMBALI : ",kembalian)

if totalmkn >= uang :
    print("Uang Anda Tidak Cukup...! \n")
    list_makanan()
else:
    list_makanan()

