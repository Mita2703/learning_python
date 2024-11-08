x = int(input("masuka nilai x :"))
y = int(input("masukan nilai y :"))
z = int(input("masukan nilai z : "))

if x > y and x > z:
    if y < z :
        print(y)
    elif z < y:
        print(z)
    print(x)
elif y > z and y > x:
    if z < x:
        print(z)
    elif x < z:
        print(x)
    print(y)
elif z > y and z > x:
    if x < y:
        print(x)
    elif y < x:
        print(y)
    print(z)