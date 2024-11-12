print('='*30)
print('\tMIL KE KILIMETER')
print('='*30)

def mil_to_kilometer(mil):
    kilometer = mil * 1.60934
    return kilometer

mil_input = float(input("Masukkan jarak dalam mil: "))
kilometer_output = mil_to_kilometer(mil_input)

print(f"{mil_input} mil sama dengan {kilometer_output:.2f} kilometer")

