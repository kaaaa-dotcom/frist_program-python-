import map

def pel7():
      while True:

      #------Program-------#
      
            this_list = ['iwan','wawan','ela'] #THIS is LIST
            print('this_list =',this_list,
                  type(this_list),
                  '\nthis_list[0] =',this_list[0],
                  '\nlen(this_list) =',len(this_list))
            this_list[2] = 'Bowo'
            print("this_list[2] = 'Bowo' =",this_list)
            
            this_list.append('Wowo')
            print("this_list.append('Wowo') =",this_list)

            this_list.insert(1, 'bambang')
            print("this_list.insert(1, 'bambang') =",this_list)

            this_tuple = ('Ehsan','Jarjit','Fizi') #THIS is TUPLE
            print(this_tuple,type(this_tuple),
                  this_tuple[0],
                  len(this_tuple))
            
            y = list(this_tuple)
            y[1] = 'ipin'
            this_tuple = tuple(y)
            print(this_tuple)
            
            x = list(this_tuple)
            x.append('Mail')
            this_tuple = tuple(x)
            print(this_tuple)

            this_set = {"Mangga","Apel","Strowberry"}
            print(this_set,
                  type(this_set),)
            
            this_set.add('Banana')
            print(this_set)

            new_set = {"MInt","spaicy"}
            this_set.update(new_set)
            print(this_set)

      #--------System---------#
            
            ex = input('\nBack ')
            if ex == '':
               map.option()
               break
            else:
               print('yang bener...!')
               break      

if __name__ == '__main__':
      pel7()