print('='*48)
print('\tHITUNG LUAS DAN KELILING TRAPESIUM')
print('='*48)

def trapesium () :
    a = int(input('nilai a\t  :  '))
    b = int(input('nilai b\t  :  '))
    c = int(input('nilai c\t  :  '))
    d = int(input('nilai d\t  :  '))
    t = int(input('nilai t\t  :  '))
    luas = lambda a,b,c,d,t : 1/2 * (a + b) * t
    keliling = lambda a,b,c,d,t : a + b + c + d

    print('Luas\t  : ',luas(a,b,c,d,t))
    print('Keliling  : ', keliling(a,b,c,d,t))

trapesium ()
