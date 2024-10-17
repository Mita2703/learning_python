jumlah = 0
for nilai in range (1,6) :
    if nilai < 5 :
        print(nilai, end= (' + '))
    else :
        print(nilai, end= (' = '))
    jumlah = jumlah + (nilai)
print(jumlah)