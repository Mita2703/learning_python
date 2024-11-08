print('='*40)
print('\tUKURAN SEPATU')
print('='*40)

ukuran = int(input('Ukuran Sepatu : '))

if ukuran >= 40 and ukuran <= 45 :
    print('BESAR')
elif ukuran >= 35 and ukuran <= 40 :
    print('SEDANG')
elif ukuran >= 30 and ukuran <=35 :
    print('KECIL')
else :
    print('TIDAK ADA')