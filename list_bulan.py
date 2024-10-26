print('='*40)
print('\tLIST BULAN')
print('='*40)

bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei','Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desemmber']
print(bulan[2])
print(bulan[9])

bulan [7] = 'August'
bulan [0] = 'January'

bulan.append('Muharam')

for i,r in enumerate (bulan):
    print(f'Bulan ke-{i+1} yaitu {r}')

