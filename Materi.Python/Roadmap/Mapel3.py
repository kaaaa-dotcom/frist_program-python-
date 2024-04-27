import map


def pel3():
      while True:
      #------Program-------#
            # NOT
            print(">>>>>This NOT")
            a = True
            c = not a
            print("data a = ",a)
            print("data c = ",c)
            
      # Logic NOT hanya 0 dan 1 sama {seperti Boolean (True,False)}

            # OR
      # Logic OR nilai akan 0 jika input 0 dan 0
            print(">>>>>This OR")
            a = False
            b = False
            c = a or b
            print(a,"OR",b,' = ', c )

            a = False
            b = True
            c = a or b
            print(a,"OR",b,'  = ', c )

            a = True
            b = False
            c = a or b
            print(a,"OR",b,'  = ', c )

            a = True
            b = True
            c = a or b
            print(a,"OR",b,'   = ', c )

            # AND
      #Logic AND nilai akan 1 jika input 1 dan 1
            print(">>>>>This AND")
            a = False
            b = False
            c = a and b
            print(a,"AND",b,' = ', c )

            a = False
            b = True
            c = a and b
            print(a,"AND",b,'  = ', c )

            a = True
            b = False
            c = a and b
            print(a,"AND",b,'  = ', c )

            a = True
            b = True
            c = a and b
            print(a,"AND",b,'   = ', c )

            # XOR
      #Logic XOR nilai akan 1 jika input berbeda as 1 dan 0 return
            print(">>>>>This XOR")
            a = False
            b = False
            c = a ^ b
            print(a,"XOR",b,' = ', c )

            a = False
            b = True
            c = a ^ b
            print(a,"XOR",b,'  = ', c )

            a = True
            b = False
            c = a ^ b
            print(a,"XOR",b,'  = ', c )

            a = True
            b = True
            c = a ^ b
            print(a,"XOR",b,'   = ', c )

      #--------------------------#


      #--------System---------#
            
            ex = input('\nBack ')
            if ex == '':
             map.option()
             break
            else:
             print('yang bener...!')
             break

      #-----------------------#

if __name__ == '__main__':
      pel3()