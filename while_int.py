count_par = 0
count_impar = 0

n = int(input("Ingrese un numero entero (-1 para detener): "))

while n != -1:
    if n % 2 == 0:
        print(n, "es par")
        count_par += 1
    elif n % 2 == 1:
        print(n, "es impar")
        count_impar += 1
    n = int(input("Ingrese un numero entero (-1 para detener): "))

print(f"Numero pares: {count_par}")
print(f"Numero impares: {count_impar}")