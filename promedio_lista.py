n = int(input("Ingrese cantidad de notas: "))
lst = []
sum = 0
i = 0

print("\nIngrese notas entre 0 y 5")

while len(lst) < n:                                         # for x in range(0,n):
    try:
        nota = float(input(f"Ingrese la nota {i+1}: "))
        if nota < 0 or nota > 5:
            print(f"\n{nota} no es valido, ingrese notas entre 0 y 5...")
            continue
    except ValueError:
        print(f"\n{nota} no es valido, Ingrese un numero...")
        continue
    lst.append(nota)
    sum += lst[i]
    i += 1
print("Su promedio es:", round(sum/n))












def promedio(n):
    lst = []
    sum = 0
    i = 0

    print("\nIngrese notas entre 0 y 5")

    while len(lst) < n:                                         # for x in range(0,n):
        try:
            nota = float(input(f"Ingrese la nota {i+1}: "))
            if nota < 0 or nota > 5:
                print(f"\n{nota} no es valido, ingrese notas entre 0 y 5...")
                continue
        except ValueError:
            print(f"\n{nota} no es valido, Ingrese un numero...")
            continue
        lst.append(nota)
        sum += lst[i]
        i += 1
    return "Su promedio es:", round(sum/n)

print(promedio(int(input("Ingrese cantidad de notas: "))))