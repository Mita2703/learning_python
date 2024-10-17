print("="*30)
print("HITUNG LUAS PERSEGI")
print("="*30)

def persegi ( ) :
    sisi = int(input('sisi\t\t: '))
    luas =  lambda s : s * s
    keliling = lambda s : 4 * s

    print('Luas\t\t: ', luas(sisi), 'cm2')
    print('Keliling\t: ', keliling(sisi), 'cm')

persegi ()
persegi ()
