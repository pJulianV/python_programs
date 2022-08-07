def int_validator(label):
    while True:
        try:
            data = int(input(label))
            break
        except ValueError:
            print("Ingrese un dato entero!")
    return data

def busqueda(lst_nums, lst_busqu, dict_position):
    for i in range(len(lst_nums)):
        if lst_nums[i] in lst_busqu: # * Mala idea es mejor guardar las busquedas depues de usarlas
            dict_position[lst_nums[i]] = i
            print(dict_position)
    return False


lst_nums = []
lst_busqu = []
dict_position = {}

n_nums = int_validator("Ingrese cantidad de numeros a ingresar: ")
for i in range(n_nums):
    lst_nums.append(int_validator("Ingrese numero: "))

n_busqueda = int_validator("Ingrese cantidad de busquedas a ingredas: ")
for i in range(n_busqueda):
    lst_busqu.append(int_validator("Ingrese numero a buscar: "))

posicion = busqueda(lst_nums, lst_busqu, dict_position)

print(dict_position)

if len(dict_position) == 0:
    print("No hay ningun elemento")
else: 
    for n in (lst_nums):
        print(dict_position[i])