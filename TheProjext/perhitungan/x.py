from add import head
import central

def satu():

    def dua(num):

            if num <= 1:
                return False
            
            for i in range(2, num):

                if num % i == 0:
                    return False
            
            return True
    try:
        
        head("MENENTUKAN BILANGAN PRIMA")

        print("___________________________")
        num = int(input("\n  Masukan angka : "))
        print("___________________________")

        if dua(num):
            print(f"\n{num} ini bilangan prima\n")
        else:
            print(f"\n{num} ini bukan bilangan prima\n")
            
    except ValueError as e:
            print(f"Input Eror di {e}")


if __name__=="__main__":
    satu()





