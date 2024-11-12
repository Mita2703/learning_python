print('='*30)
print('\tKPK DAN FPB')
print('='*30)


import math

angka1 = int(input("Tulis angka pertama\t= "))
angka2 = int(input("Tulis angka kedua\t= "))

fpb = math.gcd(angka1, angka2)
kpk = (angka1 * angka2) // fpb

print(f"FPB dari {angka1} dan {angka2} \t= {fpb}")
print(f"KPK dari {angka1} dan {angka2} \t= {kpk}")