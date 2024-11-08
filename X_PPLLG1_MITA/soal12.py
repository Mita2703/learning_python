siswa = (input('masukkan nama siswa\t\t: '))
nilai = float(input('masukkan nilai siswa (0-100)\t:'))

if 90 <= nilai <= 100: grade = 'a'
elif 80 <= nilai <= 90: grade = 'b'
elif 70 <= nilai <= 80: grade = 'c'
elif 60 <= nilai <= 70: grade = 'd'
else : grade = 'f'

print('nama siswa\t:', siswa)
print('nilai\t\t:', nilai)
print('grade\t\t:', grade)