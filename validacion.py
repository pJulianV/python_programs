#Validación Ejercicio - Tarifa Energía
nombre = input("Ingrese el Nombre del Usuario: ")
#Validación estrato (Tipo de dato y rango)
while True:
    try:
        estrato = int(input("Ingrese el estrato del usuario (1,2,3,4,5): "))
        if estrato < 1 or estrato > 5:
            print("El estrato debe ser 1,2,3,4, o 5 ")
            continue
        break
    except ValueError:
        print("*****El estrato debe ser un dato entero*****")
#Condicion
if estrato == 1:
    tb = int(10000)
elif estrato == 2:
    tb = int(15000)
elif estrato == 3:
    tb = int(30000)
elif estrato == 4:
    tb = int(50000)
else:
    tb = int(65000)
#Salidas
print("El nombre del usuario es: ", nombre)
print("El estrato del usuario es: ", estrato)
print("Tarifa Base a pagar según el estrato: ", tb)
