n = int(input("N Docentes: "))
total_honorarios = 0
count_a = 0
count_b = 0
count_c = 0
for k in range(n):
    documento = int(input("Documento: "))
    nombre = input("Nombre: ")

    categoria = input("Categoria A, B o C: ")

    horas = int(input("Horas: "))
    if categoria.upper() == "A":
        honorarios = horas * 25000
        count_a += 1
    elif categoria.upper() == "B":
        honorarios = horas * 35000
        count_b += 1
    elif categoria.upper() == "C":
        honorarios = horas * 50000
        count_c += 1
    total_honorarios += honorarios
    print(nombre, honorarios)
print(nombre, total_honorarios)
print(count_a)
print(count_b)
print(count_c)