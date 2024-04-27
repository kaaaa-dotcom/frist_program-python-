import map

def pel4():
      while True:
      #------Program-------#
            
            userinput = float(input("Masukan Angka yang bernilai\nKurang Dari 3\nAtau\nlebih dari 10\n:"))
            #Kurang Dari 3<<<
            x0 = (userinput < 3)
            print("kurang dari 3",x0)

            #Lebh dari 10>>>
            x1= (userinput > 10)
            print("lebih dari 10",x1)

            #Kurang Dari 3<<< Mix Lebih dari 10>>>
            correct = x0 or x1
            print("correct is: ",correct,"\n")

            userinput = float(input("Masukan Angka yang bernilai\nLebih Dari 3\nDan\nKurang dari 10\n:"))
            #Lebih Dari 3>>>
            y0 = (userinput > 3)
            print("Lebih Dari 3",y0)

            #Kurang Dari 10>>>
            y1 = (userinput < 10)
            print("Kurang Dari 10",y1)

            #Kurang Dari 3<<< Mix Kurang dari 10>>>
            correct = y0 and y1
            print("correct is: ",correct)

            #PR
            print(('-')*40)
            print('\tPR')
            print(('-')*40, '\n')

            # SOAL PERTAMA 
            print(">>>>> SOAL PERTAMA\n ")
            userinput = float(input("Masukan Angka yang bernilai\nLebih Dari 15\nDan\nlKurang Dari 25\nAtau\nLebih Dari 35\nDan\nKurang Dari 45\n: "))
            A1 = (userinput > 15)
            print("Lebih Dari 15",A1)

            A2 = (userinput < 25)
            print("Kurang Dari 25",A2)

            A3 = (userinput > 35)
            print("Lebih Dari 35",A3)

            A4 = (userinput < 45)
            print("Kurang Dari 45",A4)

            correct = A1 and A2 or A3 and A4
            print("correct is: ",correct,'\n')

            # SOAL KEDUA
            print(">>>>> SOAL KEDUA\n ")
            userinput = float(input("Masukan Angka yang bernilai\nKurang Dari 15\nAtau\nlLebih Dari 25\nDan\nKurang Dari 35\nAtau\nLebih Dari 45\n: "))
            A1 = (userinput < 15)
            print("Lebih Dari 15",A1)

            A2 = (userinput > 25)
            print("Kurang Dari 25",A2)

            A3 = (userinput < 35)
            print("Lebih Dari 35",A3)

            A4 = (userinput > 45)
            print("Kurang Dari 45",A4)

            correct = A1 or A2 and A3 or A4
            print("correct is: ",correct)


      #--------System---------#
            
            ex = input('\nBack ')
            if ex == '':
                  map.option()
                  break
            else:
                  print('yang bener...!')
                  break


if __name__ == '__main__':
      pel4()