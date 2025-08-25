def faktorial(x):
    if x == 0:
        return 1
    else:
        return x * faktorial(x-1)

masukan = input("masukkan angka: ")
try:
    angka_masukan = int(masukan)
    if angka_masukan < 0:
        print("Faktorial tidak bisa dihitung untuk bilangan negatif")
    else:
        hasil = faktorial(angka_masukan)
        print(f"{angka_masukan}! adalah {hasil}")
except ValueError:
    print("Input salah, silahkan coba lagi")