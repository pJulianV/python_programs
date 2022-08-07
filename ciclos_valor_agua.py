n = int(input("Cuantas personas: "))

for i in range(n):
    print(f"\nDatos usuario", i+1)
    codigo = input("Ingrese codigo: ")
    nombre = input("Ingrese nombre: ")
    estado = input("Ingrese estado (V=Vigente o S=Suspendido): ")

    while True:
        estrato = int(input("Ingrese estrato 1, 2, 3, 4, 5 o 6: " ))
        if estrato in range(1, 7):
            break
        print("\nIngrese un estrato valido")
    consumo = int(input("Ingrese consumo mensual (cm3): "))
    
    if estado.upper() == "V":
        if estrato == 1:
            tarifa_basica = 10000
        elif estrato == 2:
            tarifa_basica = 20000
        elif estrato == 3:
            tarifa_basica = 30000
        elif estrato == 4:
            tarifa_basica = 45000
        elif estrato == 5:
            tarifa_basica = 60000
        else:
            tarifa_basica = 70000

        valor_consumo = consumo * 200
        valor_pagar = valor_consumo + tarifa_basica

        print("\nNombre:", nombre)
        print("Codigo:", codigo)
        print("Valor consumo:", round(valor_consumo, 2))
        print("Valor a pagar:", round(valor_pagar, 2))
