# kita akan membuat sistem program kasir dari pyhton
def kasir(): #ini sebuah function
    print('_____PLEASE PROCESS YOUR PAYMENT_____')
    price = int(input('Input Price: '))
    money = int(input('Payment Here: '))
    minus = money - price
    
    if money >= price :
        print('Your Minus ', minus)
    else:
        print('Sorry Less Money')

    if money <= price :
        money2 = int(input('Please Buy Again: '))
        minus2 = money2 - price
        print('Your Minus ', minus2)
        print('Payment Successfull,Please Buy More')
    else:
        print('Payment Successfull,Please Buy More')
        
while True:
    Choose = int(input('1.Continue\n2.Back\n\nInput Number: '))
    if Choose == 1 :
        kasir()
    else:
        break
#UNTUK PENAMBAHAN FITUR KITA MULAI DARI PENAMBAHAN BARANG DAN SUB TOTAL
