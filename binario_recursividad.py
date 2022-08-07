def ordenar_burbuja(arr): # ! Es necesario que la lista este ordenada
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
    return arr

# * Ordenamiento recursivos para

def particion(arr):
    pivote = arr[0]
    mayores = []
    menores = []
    for i in range(1, len(arr)): 
        if arr[i] > pivote:
            mayores.append(arr[i])
        else: # elif arr[i] < pivote:  # omite los (reptetidos)
            menores.append(arr[i])
    return menores, pivote, mayores

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        menores, pivote, mayores = particion(arr)
        print(menores, pivote, mayores)
        return quicksort(menores) + [pivote] + quicksort(mayores) # ? El pivote siempre queda en la mitad y en cada "iteracion" se definen menores y mayores y se ordenan
# * [5, 2, 8, 9, 4, 7, 6]
# * [2, 4],   [5]    ,[8, 9, 7, 6]
# * [2, 4],       [5]        ,[7, 6]   [8]   [9]
# *   ^                         ^             ^   len(arr) < 2


def busqueda_binario_recursiva(lista, busqueda, izq, der):    
    if izq > der:
        print("izq > der")
        return -1
    med = (izq + der)//2 # * Dependiendo de este valor se definira si ir a la izquierda o derecha
    print(med)
    if lista[med] == busqueda:
        print("lista[med] == busqueda")
        return med
    elif lista[med] > busqueda:
        print("lista[med] > busqueda")
        return busqueda_binario_recursiva(lista, busqueda, izq, med-1)        
    else:
        print("lista[med] < busqueda")
        return busqueda_binario_recursiva(lista, busqueda, med+1, der)

def int_validator(label):
    while True:
        try:
            data = int(input(label))
            break
        except ValueError:
            print("Enter a integer value")
    return data

n = int_validator("Enter number of items in the list: ")
arr = []
for i in range(n):
    arr.append(input(f"Enter element {i+1}: "))
print(arr)

arr = quicksort(arr)
print(arr)

n_search = int_validator("Enter a number of search: ")

for i in range(n_search):
    search = input("Enter a search: ")
    position = busqueda_binario_recursiva(arr, search, 0, len(arr)-1)
    if position == -1:
        print(f"{search} isn't in the list")
    else:
        print(f"{search} is in the position {position} of the list")
