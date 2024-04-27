import map

def pel5():
      while True:

      #------Program-------#

            a = 5
            print("Nilai ",a)
            a += 1 # equal a = a + 1
            print("Nilai a += 1 ",a)
            a -= 1 # equal a = a - 1 
            print("Nilai a -= 1 ",a)
            a *= 1 # equal a = a * 1
            print("Nilai a *= 1 ",a)
            a /= 1 # equal a = a / 1
            print("Nilai a /= 1 ",a)

            b = 10 
            print("\nNilai ",b)
            b %= 3
            print("Nilai b %= 3 ",b)

            b = 10 
            print("\nNilai ",b)
            b //= 3
            print("Nilai b //= 3 ",b)
            
            b = 5
            print("\nNilai ",b)
            b **= 3
            print("Nilai b **= 3 ",b)

            c = True
            print("\nNilai c =",c)
            c |= False 
            print("Nilai c |= False =",c)


      #--------System---------#
            
            ex = input('\nBack ')
            if ex == '':
                  map.option()
                  break
            else:
                  print('yang bener...!')
                  break

if __name__ == '__main__':
      pel5()