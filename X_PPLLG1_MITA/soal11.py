harga_barang = int(input('masukkan harga barang\tv: '))

if int(harga_barang)>= 100000 : 
    diskon = harga_barang*0.05 # diskon 5%
    harga_barang = harga_barang-diskon

    print('POTONGAN HARGA\t\t :', diskon)
    print('TOTAL YANGHARUS DIBAYAR : ', harga_barang)

else:
    print('barang tidak mendapat diskon')









