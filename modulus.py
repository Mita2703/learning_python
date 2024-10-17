print('='*60)
print('\t\tDETIK KE MENIT KE JAM KE HARI')
print('='*60)

DETIK_KE_MENIT = 60
DETIK_KE_JAM = 60 * 60
DETIK_KE_HARI = 60 * 60 *24

detik = int(input('DETIK :  '))

hari = int(detik / DETIK_KE_HARI)
detik = detik % DETIK_KE_HARI

jam = int(detik / DETIK_KE_JAM)
detik = detik % DETIK_KE_JAM

menit = int(detik / DETIK_KE_MENIT)
detik = detik % DETIK_KE_MENIT

print('ADALAH : ', hari, 'hari', jam, 'jam', menit, 'menit', detik, 'detik')