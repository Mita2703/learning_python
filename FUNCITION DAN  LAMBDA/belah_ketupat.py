print('='*52)
print('\tHITUNG LUAS DAN KELILING BELAH KETUPAT')
print('='*52)

def belah_ketupat () :
    d1 = int(input('diagonal1\t\t:  '))
    d2 = int(input('diagonal2\t\t:  '))
    sisi = int(input('sisi\t\t\t:  '))
    luas = lambda d1,d2,s : 1/2 * d1 * d2
    keliling = lambda d1,d2,s : 4 * s

    print('Luas\t\t\t: ', luas(d1,d2,sisi))
    print('Keliling\t\t: ', keliling(d1,d2,sisi))

belah_ketupat()
belah_ketupat()

