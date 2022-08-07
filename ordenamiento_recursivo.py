def particion(arr): # * Divide en sublistas
    pivote = arr[0]
    mayores = []
    menores = []
    for i in range(1,len(arr)):
        if arr[i] < pivote:
            mayores.append(arr[i])
        else: 
            menores.append(arr[i])
    return pivote,mayores,menores

def quicksort(arr): # * Dividir en sublistas hasta que se ordene
    if len(arr) < 2:
        return arr
    else:
        pivote,mayores,menores = particion(arr)
        return quicksort(menores) + [pivote] + quicksort(mayores)

def int_validator(label):
    while True:
        try:
            data = int(input(label))
            break
        except ValueError:
            print("Invalid value, enter a integer value")
    return data

n = int_validator("Enter the number of items in the list: ")
list = []
for i in range(n):
    list.append(float(input(f"Item {i}: "))*1)
print(list)
print(quicksort(list))