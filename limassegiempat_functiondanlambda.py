print('='*64)
print('\tHITUNG LUAS PERMUKAAN DAN VOLUME LIMAS SEGIEMPAT')
print('='*64)

def limas_persegi_empat () :
    luas_alas = int(input('Luas alas\t\t\t:  '))
    luas_selubung_limas = int(input('Luas selubung limas\t\t:  '))
    tinggi = int(input('Tinggi\t\t\t\t:  '))
    luas_permukaan  = lambda la,ls,t : luas_alas + luas_selubung_limas
    volume = lambda la,ls,t : 1/3 * luas_alas * tinggi

    print('luas permukaan\t\t\t: ', luas_permukaan(luas_alas,luas_selubung_limas,tinggi))
    print('volume\t\t\t\t: ',volume(luas_alas,luas_selubung_limas,tinggi))

limas_persegi_empat ()