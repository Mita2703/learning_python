print("="*46)
print("\tMENGHITUNG LUAS DAN KELILING KUBUS")
print("="*46)

def kubus () : 
    sisi = int(input('sisi\t\t:  '))
    luas = lambda s : 6 * (sisi * sisi)
    keliling = lambda s : 12 * sisi 

    print('Luas\t\t: ', luas(sisi))
    print('Keliling\t: ', keliling(sisi))

kubus ()
kubus ()