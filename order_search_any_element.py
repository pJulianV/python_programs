def int_validator(label):
    while True:
        try:
            return int(int(input(label)))
            break
        except ValueError:
            print("Ingrese un valor entero")

def ordenamiento_lineal(lista):
    # lista.sort()
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                t = lista[i]
                lista[i]=lista[j]
                lista[j]=t
    return lista


def busqueda(lst, lst_busqueda, lst_position):
    for i in range(len(lst)):
        if lst[i] in lst_busqueda:
            lst_position.append(i)
    return lst_position

lst_items = []
lst_busqueda = []
lst_position = []

n_elementos = int_validator("Ingrese cantidad de elementos:\n")
for i in range(n_elementos):
    lst_items.append(input(f"Ingrese elemento {i+1}:\n"))

lst_items = ordenamiento_lineal(lst_items)
print(f"Su lista:{lst_items}")

n_busquedas = int_validator("Ingrese cantidad de busquedas\n")
for i in range(n_busquedas):
    lst_busqueda.append(input(f"Ingrese busqueda {i+1}:\n"))

lst_position = busqueda(lst_items, lst_busqueda, lst_position)
if len(lst_position) == 0:
    print("No se encontro ninguna de sus busquedas")
else:
    for i in range(len(lst_position)):
        print(f"{lst_busqueda[i]} se encuentra en la posicion {lst_position[i]}")
