print('='*44)
print('\t\tNILAI UJIAN')
print('='*44)

nilai_ujian = int(input('Nilai Ujian\t: '))

if nilai_ujian >=75 and nilai_ujian <=100 :
    print('LULUS')
elif nilai_ujian <=75 :
    print('TIDAK LULUS')
else :
    print('NILAI SALAH')
