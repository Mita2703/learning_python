print("="*43)
print("\tINFORMASI JUKNIS PERLOMBAAN")
print("="*43)

print("="*30)
print("1. JUKNIS LOMBA FUTSAL")
print("2. JUKNIS LOMBA VOLI")
print("3. JUKNIS LOMBA BASKET")
print("4. JUKNIS LOMBA BADMINTON")
print("="*30)

informasi = int(input("MASUKAN NOMOR INFORMASI LOMBA APA? : "))

if informasi == 1:
    print('''
    LOMBA FUTSAL DIMULAI HARI SENIN TANGGAL 27-9-2024
    PERJURUSAN ANGKATAN
    KETENTUAN:
    1. Peserta asli siswa/i SMKN 1 Cianjur.
    2. Setiap tim beranggotakan maksimal 8 orang pemain, yaitu 5 pemain inti danmaksimal 3 pemain cadangan.
    3. Setiap Jurusan angkatan wajib mengirimkan 1 team futsal. Jika tidak maka dikenai sanksi.
    4. Pemain diwajibkan menjunjung tinggi sportivitas dan anti-diskriminasi SARA.
    5. Suporter harus tertib tidak rusuh.
    6. Kostum atau seragam tim wajib sama dalam satu tim (panitiamenyediakan rompi).
    7. Memakai kaos kaki & menggunakan sepatu yang sesuai.
    8. Memakai Skin Deker.
    9. Tidak diperkenankan menggunakan aksesoris yang dapat membahayakan pemain lain.
    10. Keputusan wasit tidak dapat diganggu gugat.
    ''')
elif informasi == 2:
    print(''' LOMBA BOLA VOLI DIMULAI HARI SELASA TANGGAL 27-9-2024
    PERJURUSAN ANGKATAN
    KETENTUAN:
    1. Peserta asli siswa/i SMKN 1 Cianjur.
    2. Setiap Jurusan angkatan wajib mengirimkan 1 team. Jika tidak maka dikenai sanksi.
    3. Sebuah tim bisa terdiri dari maksimal 12 pemain.
    4. Menggunakan peraturan 
    5. Pemain diwajibkan menjunjung tinggi sportivitas dan anti-diskriminasi SARA.
    6. Suporter harus tertib tidak rusuh.
    7. Memakai kaos kaki & sepatu yang sesuai
    8. Pemain hanya boleh berada di areanya sendiri, tidak boleh masuk area lawan.
    9. No rasis.
    10.Mengikuti arahan panitia
    ''')
elif informasi == 3:
    print(''' LOMBA BOLA BASKET DIMULAI HARI RABU TANGGAL 28-9-2024
    PERJURUSAN ANGKATAN
    KETENTUAN:
    1. Peserta asli siswa/i SMKN 1 Cianjur.
    2. Setiap jurusan angkatan wajib mengirimkan 1 team. Jika tidak maka dikenai sanksi.
    3. Tiap team terdiri dari 10 orang pemain, (5 pemain Utama dan 5 Pemain Cadangan).
    4. Pada saat permainan berlangsung setiap team diberikan time out 1X dalam 1 Quarter (waktu time out 30 detik).
    5. Tidak ada menukar/meminjam pemain dari kelas lain.
    6. Jika team belum hadir saat pertandingan (maksimal 3 menit) maka akan di WO.
    7. Memakai kaos kaki & sepatu yang sesuai.
    8. Pemain diwajibkan menjunjung tinggi sportivitas dan anti-diskriminasi SARA.
    9. Suporter harus tertib tidak rusuh.
    10.Mengikuti arahan panitia.''')
elif informasi == 4:
    print(''' LOMBA BADMINTON DIMULAI HARI RABU TANGGAL 25-9-2024
    PERJURUSAN ANGKATAN
    KETENTUAN:
    1. Peserta asli siswa/i SMKN 1 Cianjur.
    2. Setiap jurusan angkatan wajib mengirimkan 1 team. Jika tidak maka dikenai sanksi.
    3. Menyiapkan 1 team ganda campuran
    4. Peserta memakai pakaian olahraga yang sopan
    5. Peserta membawa peralatan olahraga sesuai kebutuhannya masing-masing.
    6. Peserta hadir tepat waktu.
    7. Memakai kaos kaki & sepatu yang sesuai.
    8. Pemain diwajibkan menjunjung tinggi sportivitas dan anti-diskriminasi SARA.
    9. Suporter harus tertib tidak rusuh.
    10. Mengikuti arahan panitia. ''')