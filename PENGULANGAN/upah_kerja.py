print('='*40)
print('\t\tUPAH KERJA')
print('='*40)

golongan = input('Golongan\t\t: ')
jam_kerja = int(input('Jam Kerja\t\t: ' ))

if golongan == 'A' :
    upah_per_jam = 35000
elif golongan == 'B' :
    upah_per_jam = 30000
elif golongan == 'C' :
    upah_per_jam = 25000
elif golongan == 'D' :
    upah_per_jam = 20000

total_upah = jam_kerja * upah_per_jam

if jam_kerja - 24 > 0 :
    total_upah = total_upah + ((jam_kerja - 24)* 4000)
    print('Hasil Upah Kerja Lembur :','Rp', total_upah)

print('Hasil Upah Bersih\t:','Rp', total_upah + (jam_kerja))