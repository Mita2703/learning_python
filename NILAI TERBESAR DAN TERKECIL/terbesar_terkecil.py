print('='*40)
print('\tNILAI TERBESAR DAN TERKECIL')
print('='*40)

nilai1 = int(input('Masukkan Nilai 1 : '))
nilai2 = int(input('Masukkan Nilai 2 : '))
nilai3 = int(input('Masukkan Nilai 3 : '))

max = 0
min = 0

if nilai1 > nilai2 :
    max = nilai1
else :
    max = nilai2
if nilai3 > max :
    max = nilai3

if nilai1 < nilai2 :
    min = nilai1
else :
    max = nilai2
if nilai3 < min :
    min = nilai3

print('Nilai Terbesar : ',max)
print('Nilai Terkecil : ',min)