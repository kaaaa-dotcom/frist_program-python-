def Spec():
    try:
        number = int(input("how if..? "))
        if number % 2 == 0:
            print(f"The number {number} is genap")
        else:
            print(f"The number {number} is ganjil")
    except ValueError as e:
        print(f'There is Eror ({e}) input just number 😁 ')

if __name__ == '__main__':
    Spec()
        

   