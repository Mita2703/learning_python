print("="*60)
print("MENCETAK APAKAH ANGKA DALAM DAFTAR ADALAH GANJIL ATAU GENAP")
print("="*60)

numbers = [3, 45, 7, 56, 88]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} adalah angka genap")
    else:
        print(f"{num} adalah angka ganjil")