print('='*32)
print('\tGANJIL DAN GENAP')
print('='*32)

awal = int(input('Nilai Awal : '))
akhir = int(input('Nilai akhir : '))

ganjil = []
genap = []

for rm in range (awal,akhir + 1 ) :
    if rm%2 == 1 :
        ganjil.append(rm) 
    if rm%2 == 0 :
        genap.append(rm)

print('Nilai Ganjil : ',ganjil)
print('Nilai Genap  : ',genap)