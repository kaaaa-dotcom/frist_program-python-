import map

def pel6():
      while True:
      #------Program-------#
         
         hee = input('If input ')
         if hee == 'Hee':
            print(':',True)
         elif hee != 'Hee':
            print(':',False)
         else:
            print('😀')


      #--------System---------#
            
         ex = input('\nBack ')
         if ex == '':
               map.option()
               break
         else:
               print('yang bener...!')
               break

if __name__ == '__main__':
    pel6()