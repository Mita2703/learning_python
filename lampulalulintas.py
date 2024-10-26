print('='*49)
print('\t\tLAMPU LALU LINTAS')
print('='*49)

status_lampu = input('Status Lampu : ')
warna_lampu = input('Warna Lampu  : ')

if status_lampu == 'menyala' : 
    if warna_lampu == 'merah' :
        print('BERHENTI')
    elif warna_lampu == 'kuning' :
        print('BERSIAP')
    elif warna_lampu == 'hijau' :
        print('JALAN')
    else :
        print('Nothing')
else :
    print('EROR --')