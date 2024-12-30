import random

# Simulasi melempar dadu
def lempar_dadu():
    return random.randint(1, 6)  # Menghasilkan angka acak antara 1 dan 6

# Menghitung peluang mendapatkan angka ganjil
def peluang_angka_ganjil():
    angka = lempar_dadu()
    if angka in [1, 3, 5]:
        return True
    else:
        return False

# Simulasi percobaan melempar dadu dan menghitung peluang
total_percobaan = int(input("Masukan total percobaan : "))
jumlah_kejadian = sum(peluang_angka_ganjil() for _ in range(total_percobaan))
peluang = jumlah_kejadian / total_percobaan

print(f"Peluang mendapatkan angka ganjil: {peluang}")