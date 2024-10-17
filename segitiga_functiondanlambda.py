print("="*36)
print("\tHITUNG LUAS SEGITIGA")
print("="*36)

def segitiga () :
    alas = int(input('Alas\t\t:  '))
    tinggi = int(input('Tinggi\t\t:  '))
    luas = lambda a,t : 1/2 * alas * tinggi

    print('Luas segitiga\t: ', luas(alas,tinggi))

segitiga ()
segitiga ()
