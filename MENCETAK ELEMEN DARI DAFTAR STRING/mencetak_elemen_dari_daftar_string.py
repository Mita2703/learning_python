print("="*40)
print("MENCETAK ELEMEN DARI DAFTAR STRING")
print("="*40)

word = "hello everyone, let me introduce my self"
vowels = "aeiou"
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print("Jumlah huruf vokal:", count)