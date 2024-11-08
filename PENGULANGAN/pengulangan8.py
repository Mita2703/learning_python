print('='*30)
print('\tPENGULANGAN')
print('='*30)

jumlah = 0
for p in range(2, 11, 2) :
    if p < 10 : 
        print(p , end= ' + ')
    else :
        print(p, end= ' = ')
    jumlah = jumlah + p
print(jumlah)