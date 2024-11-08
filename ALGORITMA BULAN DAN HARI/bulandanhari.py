print ("="*40)
print ("\tALGORITMA BULAN DAN HARI")
print ("="*40)

nama_bulan = (input("masukan nama bulan\t:  "))

if nama_bulan == "Januari" : 
    jumlah_hari = "31 hari"
elif nama_bulan == "Februari":
    jumlah_hari = "29 hari"
elif nama_bulan == "Maret":
    jumlah_hari = "31 hari"
elif nama_bulan == "April":
    jumlah_hari = "30 hari"
elif nama_bulan == "Mei":
    jumlah_hari = "31 hari"
elif nama_bulan == "Juni":
    jumlah_hari = "30 hari"
elif nama_bulan == "Juli":
    jumlah_hari = "31 hari"
elif nama_bulan == "Agustus":
    jumlah_hari = "31 hari"
elif nama_bulan == "September":
    jumlah_hari = "30 hari"
elif nama_bulan == "Oktober":
    jumlah_hari = "31 hari"
elif nama_bulan == "November":
    jumlah_hari = "30 hari"
elif nama_bulan == "Desember":
    jumlah_hari = "31 hari"
else:
    nama_bulan = "NO MORE"
print('Jumlah hari\t\t: ', jumlah_hari)