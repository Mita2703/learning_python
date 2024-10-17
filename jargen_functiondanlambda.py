print("="*52)
print("\tHITUNG LUAS DAN KELILING JAJAR GENJANG")
print("="*52)

def jajar_genjang () :
    a = int(input('nilai a\t\t:  '))
    b = int(input('nilai \t\t:  '))
    alas = int(input('alas\t\t:  '))
    tinggi = int(input('tinggi\t\t:  '))
    luas = lambda a,b,l,t : a * tinggi
    keliling = lambda a,b,l,t : 2 * (a + b)

    print('Luas\t\t: ', luas(a,b,alas,tinggi))
    print('Keliling\t: ',keliling(a,b,alas,tinggi))

jajar_genjang ()
jajar_genjang ()
