print('='*55)
print('\t RUMUS VOLUME DAN LUAS PERMUKAAN TABUNG')
print('='*55)

jari_jari = int(input('masukkan nilai jari - jari\t: '))
phi = 3.14
tinggi = int(input('masukkan nilai tinnggi\t: '))

volume = 2 * jari_jari * tinggi 
luas_permukaan = phi * jari_jari + 2 * phi * jari_jari * tinggi

print('volumenya adalah =', volume, 'cm2')
print('luas permukaaanya adalah =', luas_permukaan, 'cm')

