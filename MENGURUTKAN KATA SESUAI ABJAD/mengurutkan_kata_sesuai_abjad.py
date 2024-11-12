print('='*45)
print('\tMENGUTKAN KATA SESUAI ABJAD')
print('='*45)

kalimat = input("Tulis Kalimat: ")
 
kata = kalimat.split()
 
kata.sort()
 
print("Berikut Urutan Kata-Kata:")
for urut in kata:
   print(urut)