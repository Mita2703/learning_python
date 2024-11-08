print("="*64)
print("\tHITUNG LUAS PERMUKAAN DAN VOLUME PRISMA SEGIEMPAT")
print("="*64)

luas_alas = int(input('masukkan angka\t: '))
keliling_alas = int(input('masukkan angka\t: '))
tinggi = int(input('masukkan angka\t: '))
panjang = int(input('masukkan angka\t: '))
lebar = int(input('masukkan angka\t: '))

luas_permukaan = (2 * luas_alas) + (keliling_alas * tinggi)
volume = panjang * lebar * tinggi

print("luas permukaan prisma segiempat\t:", luas_permukaan, 'cm3')
print('volume prisma segiempat\t:', volume, 'cm3')
