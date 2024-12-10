print("=" * 60)
print('''\t\t\tHallo!\r
\t\tSelamat Datang Di Restoran Mini\r
''', "=" * 60)

nama = input("Siapa Nama Kamu \t= ")
waktu = input("Tanggal Kamu Membeli\t= ")
print('''
''')

print("=" * 60)
print("\t\t", "" * 5, "Silahkan Pilih Menu", "" * 5)
print("=" * 60)

print('''1. Air Asing\t\tRp.4.000\r
2. Nasi Goreng Jeruk\t\tRp.20.000\r
3. Pangsit Jebew\t\tRp.10.000\r
4. Mie Ayam\t\tRp.10.000\r
''')
h = []
a = 1

menu = int(input("Menu Nomor Berapa Yang Ingin Kamu Pesan = "))
if menu == 1:
    harga = 4000
elif menu == 2:
    harga = 20000
elif menu == 3:
    harga = 10000
elif menu == 4:
    harga = 10000
else:
    while True:
        print("Maaf Menu Tidak Tersedia Silahkan Pilih Menu Lain Ya")
        if menu == 1 or menu == 2 or menu == 3 or menu == 4:
            if menu == 1:
                harga = 4000
            elif menu == 2:
                harga = 20000
            elif menu == 3:
                harga = 10000
            elif menu == 4:
                harga = 10000
                break

jumlah = int(input("Berapa Jumlah Yang Ingin Kamu Beli = "))
for i in range(jumlah):
    h.append(harga)

while True:
    jawab = input("Apakah Ada Yang Pesanan Yang Ingin Ditambah/dikurangi ? tambah/kurang/tidak = ")
    if jawab == "tambah":
        tambah = int(input("Masukan Nomor Pesanan Yang Ingin Ditambahkan = "))
        if tambah == 1:
            harga = 4000
        elif tambah == 2:
            harga = 20000
        elif tambah == 3:
            harga = 10000
        elif tambah == 4:
            harga = 10000
        jumlah_tambahan = int(input("Berapa Jumlah Pembelian = "))
        for i in range(jumlah_tambahan):
            h.append(harga)
        c = jumlah_tambahan + jumlah
        print("Total Pesanan Anda = ", c)
        bayar = sum(h)
        print("Total Pembayaran =  Rp.{}".format(bayar))
        break
    elif jawab == "kurang":
        kurang = int(input("Berapa Jumlah Yang Kurang = "))
        for i in range(kurang):
            if kurang <= 1:
                a -= kurang
                del h[a]
                bayar = sum(h)
                break
            else:
                kurang -= a
                del h [kurang]
                if kurang < 0:
                    break
            c = jumlah - kurang
            print ("Total Pesanan Anda = ", c)
            bayar = sum(h)
            print("Total Pembayaran = Rp.{}",format(bayar))
            break
        else:
            bayar = sum(h)
            c = jumlah
            print("Total Pemesanan = ", c)
            print("Total Pembayaran = Rp.".format(bayar))
            break