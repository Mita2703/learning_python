print("="*52)
print("\t\tRUMUS PRISMA SEGITIGA")
print("="*52)

alas = int(input("MAsukkan nilai alas\t\t :  "))
tinggi = int(input("MAsukkan nilai tinggi\t\t :  "))
keliling_alas = int(input("MAsukkan nilai keliling alas\t :  "))
tinggi_prisma = int(input("MAsukkan nilai tinggi prisma\t :  "))

luas_permukaan_prisma = (2 * 1/2 * alas * tinggi) + (keliling_alas * tinggi_prisma)
volume = (1/2 * alas * tinggi) * tinggi_prisma

print("Luas Permukaan\t\t\t : ", luas_permukaan_prisma)
print("Volume\t\t\t\t : ", volume)