print('='*30)
print('\tPENGULANGAN')
print('='*30)

jumlah = 0
for rm in range (1,6) :
    if rm < 5 :
        print(rm , end= ' + ')
    else :
        print(rm, end= ' = ' )
    jumlah = jumlah + rm
print(jumlah)