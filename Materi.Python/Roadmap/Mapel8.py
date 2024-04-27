import map

def pel8():
      while True:
      #------Program-------#

            kuadrat = lambda number:number**2
            print(f"hasil lambda kuadrat = {kuadrat(15)}")

      #--------System---------#
            
            ex = input('\nBack ')
            if ex == '':
               map.option()
               break
            else:
               print('yang bener...!')
               break

if __name__ == '__main__':
      pel8()