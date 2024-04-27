from time import sleep

def style(title):
    min = '='* (len(title))
    print(min)
    print(f'{title}')
    print(min)

def out():
    print('Materi Akan Berhenti')
    sleep(1)
    print('1')
    sleep(1)
    print('2')
    sleep(1)
    print('3')
    print('Out.....')

if __name__ == '__main__':
    style('Basic Syntax')
    out()