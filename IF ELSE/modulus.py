print('='*60)
print('\t\tDETIK KE MENIT KE JAM KE HARI')
print('='*60)

detik_ke_menit = 60
detik_ke_jam = 60 * 60
detik_ke_hari = 60 * 60 * 24

detik = int(input('DETIK\t:  '))

hari = int(detik / detik_ke_hari)
detik = detik % detik_ke_hari

jam = int(detik / detik_ke_jam)
detik = detik % detik_ke_jam

menit = int(detik / detik_ke_menit)
detik = detik % detik_ke_menit

print('ADALAH\t: ', hari, 'hari', jam, 'jam', menit, 'menit', detik, 'detik')
