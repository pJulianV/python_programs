def int_validator(label):
    while True:
        try: 
            data = int(input(label))
            break
        except ValueError:
            print("Ingrese un valor entero: ")
    return data

def metodo_burbuja(lista):
    for i in range(len(lista)-1): # * Toma todos los elementos menos el ultimo ya que ya no necesita compararse
        print("Se compara:",lista[i])
        for j in range(i+1, len(lista)): # * La posicion j toma el valor siguiente a i y compara cada i con cada j
            print("Con:",lista[j])
            if lista[i]>lista[j]:    # * Compara el elemento[i] con el siguiente elemento[i+1]
                print(f"{lista[i]} > {lista[j]}")
                t = lista[i]
                lista[i] = lista[j]
                lista[j] = t
    # * Lo anterior se repite con cada uno de lo elementos
    return lista

nums = []
n = int_validator("Ingrese la cantiad de numeros a ingresar: ")
for i in range(n):
    nums.append(int_validator(f"Ingrese dato {i+1}: "))

print(metodo_burbuja(nums))

