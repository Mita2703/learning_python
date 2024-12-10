print("="*40)
print("\tRATUSAN, RIBUAN, JUTAAN")
print("="*40)

angka = int(input("Masukkan Angka : "))

if angka >= 100 and angka < 1000 :
    print("Ratusan")
elif angka >=1000 and angka < 1000000 :
    print("Ribuan")
elif angka >= 1000000 and angka < 100000000 :
    print("Jutaan")