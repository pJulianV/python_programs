nombre = input("Ingrese su nombre: ")

while True:
    try:
        estrato = int(input("Ingrese estrato (1, 2 ,3 , 4 o 5): "))
        if estrato > 5 or estrato < 1:
            print("Ingrese un valor entre 1 y 5")
            continue
        break
    except ValueError:
        print("Ingrese un valor entero")
if estrato == 1:
    tarifa_basica = 10000
elif estrato == 2:
    tarifa_basica = 15000
elif estrato == 3:
    tarifa_basica = 30000
elif estrato == 4:
    tarifa_basica = 50000
else:
    tarifa_basica = 65000
print("Nombre:",nombre)
print("Tarifa basica:",tarifa_basica)
