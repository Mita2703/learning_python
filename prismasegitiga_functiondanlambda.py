print('='*62)
print('\tHITUNG LUAS PERMUKAAN DAN VOLUME PRISMA SEGITIGA')
print('='*62)

def prisma_segitiga () :
    alas = int(input('Alas\t\t\t:  '))
    tinggi = int(input('Tinggi\t\t:  '))
    tinggi_prisma = int(input('Tinggi prisma\t:  '))
    keliling_alas = int(input('Keliling alas\t:  '))
    luas_permukaan_prisma = lambda a,t,tp,ka : (2 * 1/2 * alas * tinggi) + (keliling_alas * tinggi_prisma)
    volume = lambda a,t,tp,ka : (1/2 * alas * tinggi) * tinggi_prisma

    print('Luas permukaan prisma\t: ', luas_permukaan_prisma(alas,tinggi,tinggi_prisma,keliling_alas,))
    print('Volume\t\t\t: ',volume (alas,tinggi,tinggi_prisma,keliling_alas,))

prisma_segitiga ()