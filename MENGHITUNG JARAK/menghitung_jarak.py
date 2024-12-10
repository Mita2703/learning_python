def hitung_jarak(v, t):
  s = v * t
  return s

kecepatan = float(input("Masukkan Kecepatan (KM/JAM) = "))
waktu = float(input("Masukkan Waktu Tempuh (JAM) = "))

jarak = hitung_jarak(kecepatan, waktu)

print("Jarak Yang Ditempuh Adalah  =", jarak, "km")