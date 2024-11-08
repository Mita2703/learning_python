print('='*40)
print('\t\tDISKON')
print('='*40)

total = int(input('Total Belanja\t\t: Rp '))
setelah_diskon = total 

if  total < 100.000 :
    diskon = total * (5/100)
else:
    diskon = total * (10/100)

setelah_diskon = total - diskon 
print("Diskon\t\t\t: Rp {:,}".format(int(diskon)).replace(',','.'))
print("Harga setelah diskon\t: Rp {:,}".format(int(setelah_diskon)).replace(',','.'))