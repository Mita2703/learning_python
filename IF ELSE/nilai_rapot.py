print('='*30)
print('\tNILAI UJIAN')
print('='*30)

nilai = int(input('Nilai\t: '))

if nilai >=80 and nilai <=100 :
    print ('A')
elif nilai >=70 and nilai <=80 :
    print('B')
elif nilai >60 and nilai <=70 :
    print('C')
elif nilai >=50 and nilai <=60 :
    print('D')
elif nilai >=40 and nilai <=50 :
    print('E')
else :
    print('TIDAK NAIK KELAS')
