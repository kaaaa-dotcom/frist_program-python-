from time import sleep

def head(title):
    xX = "="* (len(title) + 4)
    print(xX)
    print(f"= {title} =")
    print(xX)

def out():
    print("\nMesin akan mati")
    sleep(1)
    print("1")
    sleep(1)
    print("2")
    sleep(1)
    print("3")
    sleep(2)
    print("Mesin mati...")


if __name__=="__main__":
    head("SELAMAT DATANG")
    out()




