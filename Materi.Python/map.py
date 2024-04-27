from libry import style, out
from Roadmap import Mapel1, Mapel2, Mapel3, Mapel4, Mapel5, Mapel6, Mapel7, Mapel8

def option():
 choose = ('''
 1.Basic syntax
 2.Variabels And Data Type
 3.Operasi Logika atau Boolean
 4.Latihan Komparasi dan Logika
 5.Operator Assigment
 6.if-elif-else stament
 7.List,Tuple,Set,Dictonary
 8.anonymous lambda
  
 # out''')
 #----------------------------------#
 print(choose)
 min = '-'* (len('Apa yang ingin anda pelajari : '))
 print(min)
 choose = (f'{int(input('Apa yang ingin anda pelajari : '))}')
 print(min)
 #----------------------------------#

 #----------------------------------#
 if choose == '1':
  style('Basic syntax')
  Mapel1.pel1()
 elif choose == '2':
  style('Variabels And Data Type')
  Mapel2.pel2()
 elif choose == '3':
  style('Operasi Logika atau Boolean')
  Mapel3.pel3()
 elif choose == '4':
  style('Latihan Komparasi dan Logika')
  Mapel4.pel4()
 elif choose == '5':
  style('Operator Assigment')
  Mapel5.pel5()
 elif choose == '6':
  style('if-elif-else stament')
  Mapel6.pel6()
 elif choose == '7':
  style('List,Tuple,Set,Dictonary')
  Mapel7.pel7()
 elif choose == '8':
  style('anonymous lambda')
  Mapel8.pel8()
 elif choose == '9':
  out()
 else:
  print('No yang anda masukan tidak sesuai')
  option()

def main():
 option()
 


if __name__ == '__main__':
 main()