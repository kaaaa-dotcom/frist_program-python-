# kita akan membuat sistem program kasir dari pyhton
def kasir():
    print('_____PLEASE PROCESS YOUR PAYMENT_____')
    price = int(input('Input Price: '))
    money = int(input('Payment Here: '))
    minus = money - price

    if money >= price :
        print('Minus: ', minus)
    else:
        print('Sorry Less Money')

    if money <= price :
        money = int(input('Please Pay Again: '))
        print('Payment Successfull, Buy More')
    else:
        print('Payment Successfull, Buy More')


while True:
    Choose = int(input('1.Continue\n2.Back\n\nChoose Number: '))
    if Choose == 1 :
        kasir()
    else:
        break

#UNTUK PENAMBAHAN FITUR KITA MULAI DARI PENAMBAHAN BARANG DAN SUB TOTAL