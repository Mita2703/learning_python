print("\tHITUNG LUAS PERMUKAAN DAN VOLUME PRISMA SEGIEMPAT")
print("="*64)
print("="*64)

def prisma_segiempat () :
    luas_alas = int(input('luas alas\t\t:  '))
    keliling_alas = int(input('keliling alas\t\t:  '))
    tinggi = int(input('tinggi\t\t\t:  '))
    panjang = int(input('panjang\t\t\t:  '))
    lebar = int(input('lebar\t\t\t:  '))
    luas_permukaan = lambda la,ka,t,p,l : (2 * luas_alas) + (keliling_alas * tinggi)
    volume = lambda la,ka,t,p,l : panjang * lebar * tinggi

    print('Luas permukaan\t\t: ', luas_permukaan(luas_alas,keliling_alas,tinggi,panjang,lebar))
    print('Volume\t\t\t: ',volume(luas_alas,keliling_alas,tinggi,panjang,lebar))

prisma_segiempat ()
prisma_segiempat ()