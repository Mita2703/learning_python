print('='*40)
print('\t\tLOGIN')
print('='*40)

username = "mitaa"
password = "mita2703"

input_username = input('Masukkkan username : ')
input_password = input('Masukkan password  : ')

if input_username == username and input_password == password :
    print('LOGIN BERHASIL!!')

else :
    print('username atau password salah')