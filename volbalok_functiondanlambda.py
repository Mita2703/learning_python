print("="*37)
print("\tHITUNG VOLUME BALOK")
print("="*37)

def volume_balok () :
    panjang = int(input("Panjang\t: "))
    lebar = int(input("Lebar\t: "))
    tinggi = int(input("Tinggi\t: "))
    volume = lambda p,l,t : panjang * lebar * tinggi

    print('volume\t: ', volume(panjang,lebar,tinggi))

volume_balok ()