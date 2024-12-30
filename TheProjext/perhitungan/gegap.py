from add import head

def genap():

    try:

        head("MENENTUKAN GENAP & DAN GANJIL")

        bilangan = int(input("masukan angka : "))

        if bilangan % 2 == 0:
            print(f"{bilangan} termasuk bilangan genap")
        else :
            print(f"{bilangan} termasuk bilangan ganjil")
        
    except ValueError as e:
        print(f"Input Eror di {e}")

if __name__=="__main__":
    genap()