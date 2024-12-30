from perhitungan import gegap, x
from add import head, out

def main():

    try:
        
        head("SELAMAT DATANG")

        user = int(input(""" 
Menu Pilihan :
                
    1. Prima
    2. Genap & Ganjil
                            
    #. out
    _____________________________
            
            Masukan pilihan :  """))
            
        if user == 1:
            x.satu()
        elif user == 2:
            gegap.genap()
        elif user == 3:
            out()
        else:
            print("Wrooongg")
    except ValueError as e:
        print("\ninput nomor aja yaa...!!")


if __name__=="__main__":
    main()







