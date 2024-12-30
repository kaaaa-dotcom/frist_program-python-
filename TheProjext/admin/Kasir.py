from console import db2

def add_barang():
    name= input('Name item : ')
    stock= int(input('Stock item : '))
    price= int(input('Price item : '))

    db2.barang(name,stock,price)

def view():
    look = db2.view()
    for i in look:
        id=i[0]
        name=i[1]
        stock=i[2]
        price=i[3]
        print(f'''
ID :{id}
Name item :{name}
Stock item :{stock}
Price item :{price}
''')
        
def Pay():    
    # lanjjut besooooooooooooooooooookkkkkkkkkkkkkkkkkkkkkkkkk
    pass

def main():
    try:
        while True:
            menu = int(input('1.add item\n2.view item\n3.pay item\n4.Out\n\nchoice: '))
            if menu == 1:
                add_barang()
            elif menu == 2:
                view()
            elif menu == 3:
                Pay()
            elif menu == 4:
                exit()
            else:
                print('input invalid')
    except ValueError as e:
        print(f'Please just input number :{e}')

if __name__ == '__main__':
    main()