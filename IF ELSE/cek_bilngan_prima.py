print('='*56)
print('\t\tCEK BILANGAN PRIMA')
print('='*56)


nilai = int(input("Masukkan bilangan : "))

flag = False
if nilai == 1 :
    print(nilai,"adalah bukan bilangan prima")
elif nilai > 1 :
    for t in range(2,nilai):
        if nilai % t == 0 :
            flag = True
        break
if flag :
    print(nilai,"adalah bukan bilangan prima")
else :
    print(nilai,"adalah bilangan prima")




