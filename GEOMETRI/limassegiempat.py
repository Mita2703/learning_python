print("="*55)
print("\t\tRUMUS LIMAS SEGIEMPAT")
print("="*55)

luas_alas = int(input("Masukkan nilai luas alas\t:  "))
luas_selubung_limas = int(input("Masukkan nilai selubung limas   :  "))
tinggi = int(input("Masukkan nilai tinggi\t\t:  "))

luas_permukaan = luas_alas + luas_selubung_limas
volume = 1/3 * luas_alas * tinggi

print("Luas Permukaan\t\t\t: ", luas_permukaan)
print("Volume\t\t\t\t: ", volume)