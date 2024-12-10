print("="*70)
print("MENJUMLAHKAN SEMUA ANGKA DALAM DAFTAR YANG LEBIH BESAR DARI 7")
print("="*70)

numbers = [3, 5, 9, 16, 21, 44, 78]
total = 0
for number in numbers:
    if number > 7:
        total += number
print("Total:", total)