a = input("Indonesia  : ")

indonesia = ['merah', 'kuning', 'biru', 'ungu', 'putih', 'hitam', 'merah muda', 'abu -abu', 'coklat', 'hijau']
inggris = ['red', 'yellow', 'blue', 'purple', 'white', 'black', 'pink', 'grey', 'brown', 'green']

if a == 'merah' : 
    b = inggris[0]
elif  a == 'kuning' :
    b = inggris[1]
elif a == 'biru' :
    b = inggris[2]
elif a == 'ungu' :
    b = inggris[3]
elif a == 'putih' :
    b = inggris[4]
elif a == 'hitam' :
    b = inggris[5]
elif a == 'merah muda' :
    b = inggris[6]
elif a == 'abu - abu' :
    b = inggris[7]
elif a == 'coklat' :
    b = inggris[8]
elif a == 'hijau' :
    b = inggris[9]
else :
    print('terserah')

print(f'inggris    : {b}')