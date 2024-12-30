# VARIABEL : A CONTAINER HAVE VALUE
x = 'hello world'
print(x)


# TYPE DATA STRING OR STR
nama = 'Kaa'
print('nama ', nama, type(nama))
angka = '45'
print(angka, type(angka))

# TYPE DATA INTERGER OR INT
number = 30
print('number', number, 'type', type(number))

# TYPE DATA FLOATING OR FLOAT
number = 10.9
print('number', number, 'type', type(number))

# TYPE DATA BOOLEAN OR BOOL
x = True
print('nama ', x, 'type ', type(x))

# TUTORIAL CASTING 
print('_____TUTORIAL CASTING_____')
print('_____INT_____')

casting = 20

STR = str(casting)
FLOAT = float(casting)
BOOL = bool(casting)
print( STR , type(STR))
print( FLOAT , type(FLOAT))
print( BOOL , type(BOOL))

print('\n')
print('OPERASI ARITMATIKA\n') # OPERASI ARITMATIKA

a = 20
b = 5

print('OPERASI PENAMBAHAN (+)')
result = a + b 
print( a, '+', b, '=', result, '\n')

print('OPERASI PENGURANGAN (-)')
result = a - b 
print( a, '-', b, '=', result, '\n')

print('OPERASI PERKALIAN (*)')
result = a * b 
print( a, '*', b, '=', result, '\n')

print('OPERASI PEMBAGIAN (/)')
result = a / b
print( a, '/', b, '=', result, '\n')

print('OPERASI EKSPONEN (**)')
result = a ** b
print( a, '**', b, '=', result, '\n')

print('OPERASI MODULUS (%)')
result = a % b
print( a, '%', b, '=', result, '\n')

print('OPERASI FLOOR DIVIISION (//)')
result = a // b
print( a, '//', b, '=', result, '\n')

# UNTUK PACKING DAN UNPACKING

print('=====PACKING AND UNPACKING=====')

a, b, c = 10, 20, 30
d = [ a, b, c]
print(f'a = {a} b = {b} c = {c}')
print(f'd = {d}\n')

list = [ 29, 18, 48]
a, b, c = 29, 18, 48
print('list=',list)
print('a=',a, 'b=',b, 'c=',c, '\n')

# UNTUK FOR LOOPING

print('=====FOR LOOP=====')
list = [ 31, 32, 33]
for me in list:
    print(me, '\n')

# UJI COBA 

saya = 'Eka Wahyu Nugroho'
print(len(saya), '\n')
print(saya.find('a'), '\n')
print('Eka' in saya, '\n')
print('eka' in saya, '\n')

# UJI COBA2

nim = ['001', '002', '003']
nama = ['Eka', 'Wahyu', 'Nugroho']
for data_nim, data_nama in zip(nim,nama):
    print(data_nim, data_nama, '\n')

print('KONVERENSI TEMPERATUR')

celcius = float(input('Masukan Suhu: '))
print( 'suhunya adalah',celcius,'C')

reamur = (4/5)*celcius
print('Hasilnya reamur adalah',reamur,"R")

farenheit = ((9/5) * celcius) + 32
print('Hasilnya farenheit adalah',farenheit,"F")

kelvin = celcius + 273
print('Hasilnya kelvin adalah',kelvin,"K")

# LOGIKA BOOLEAN

print(True)