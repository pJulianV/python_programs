def busqueda_binaria(lst, search): # ! La lista debe estar ordenada de menor a mayor
    izq = 0 
    der = len((lst)-1)
    while izq <= der:
        med = (izq - der)//2
        print(f"Left = {izq}")
        print(f"Right = {der}")
        print(f"The center is {med}")
        if lst(med) == search:
            print(f"{lst(med)} is in {med}")
            return med
        elif lst(med) < search:
            der = med - 1
        else:
            izq = med + 1        
    return -1


def busqueda_lineal(lst, search):
    for i in range(len(lst)):
        if lst[i] == search:
            return i
        else:
            return -1

def int_validator(label):
    while True:
        try:
            data = int(input(label))
            break
        except ValueError:
            print("Enter a intenger value")
    return data


def ordenamiento_burbuja(lst):
    # sort
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t


n = int_validator("Enter quantity of numbers:\n")
nums = []
for i in range(n):
    nums.append(int_validator(f"Enter item {i+1}:\n"))
nums = ordenamiento_burbuja(nums) 

while True:
    search = input(f"Enter search\n")
    if search.upper() == "STOP":
        break
    elif int(search):
        search = int(search)
    else:
        search = int_validator("Enter search\n")
    posicion = busqueda_binaria(nums, search)
    if posicion == -1:
        print("No se encontro ningun documento")
    else:
        print(f"{search}, es el elemento {posicion+1} en los numeros")
