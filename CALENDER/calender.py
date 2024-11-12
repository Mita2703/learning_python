print("="*30)
print("\tKALENDER")
print("="*30)

import calendar


tahun = int(input("Masukkan tahun: "))
bulan= int(input("Masukkan bulan (dalam angka): "))

print(calendar.month(tahun,bulan))