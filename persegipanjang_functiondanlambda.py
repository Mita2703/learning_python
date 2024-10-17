print("="*40)
print("\tHITUNG LUAS PERSEGI PANJANG")
print("="*40)

def persegi_panjang () :
    panjang = int(input('panjang\t\t:  '))
    lebar = int(input('lebar\t\t:  '))
    luas = lambda l,p: p*l
    keliling = lambda l,p: 2 * p + l

    print('luas\t\t: ',luas(panjang,lebar))
    print('keliling\t: ', keliling(panjang,lebar))

persegi_panjang ()
persegi_panjang ()