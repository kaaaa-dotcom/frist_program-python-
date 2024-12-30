
def prima(): # function menyatakan pada bilangan

    bilangan = int(input('\nSilahkan masukan Angka : ')) # membungkus bilangan dengan variable

    if bilangan <= 1: # statment untuk mendeklarasi bahwa bilangan tidak boleh 1 atau kurang
        print(f"{bilangan} ini tidak termasuk bilangan prima")
    elif bilangan == 2:
        print(f"{bilangan} ini termasuk bilangan prima")


    for x in range(1, bilangan): # perulangan pada perhitungan dimulai dari 2 sampai angka yang di input 

        if bilangan % x == 0: # statment menyatakan perhitungan pada bilangan yang diinput sampai dengan perulangan for 
            print(f"{bilangan} ini tidak termasuk bilangan prima")
            break
        else:
            print(f"{bilangan} ini termasuk bilangan prima")
            break


if __name__=="__main__":
    prima()
    

