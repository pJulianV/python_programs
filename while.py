a = int(input("Ingrese Numero: "))
b = int(input("Ingrese Numero: "))
while a != b:
    if a > b:
        a -= 1
        b += 1
        print(a, b)
    elif a < b:
        a += 1
        b -= 1
        print(a, b)
    else:
        print(a, b)
