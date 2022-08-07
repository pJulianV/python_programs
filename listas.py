pares_100 = list(range(2,100,2))  #range(n_inicial, n_final, intervalo)
mul_4_100 = [x for x in pares_100 if x % 4 == 0]
nums = pares_100

for i in mul_4_100:
    nums.append(i)
print(nums.count(4))

# Suma de numeros
num = 0
count_n = 0
print("Escriba ")
while num != -1:
    num = int(input("Ingrese numeros: "))
    count_n += 1



txt = input("Escriba :>\n")
print(f"Su texto tiene {len(txt.split())} palabras")

vocals = ["a","e","i","o","u"]

count_vocals = 0

for d in txt:
    if d in vocals:
        count_vocals += 1

print(f"Su texto tiene {count_vocals} vocales")

txt_lst = txt.split()
print(txt_lst)

lista_comestibles = ["arroz","pan"]
lista = [1, "juan", lista_comestibles]
print(lista[2])

# Contar numero int de una lista
nums = [x for x in (range(0,101))]
nums.extend(nums)

nums.count(1)

print("Se invertira su texto: ")
word = input("Escriba: ")
print(word[::-1])

# Selecionar un elemento de subelementos de n listas

# Extend con una variable lista

lista = ["pan", "leche", "harina"]
lista_1 = ["huevos", "azucar", "chocolate"]

lista_final = lista + lista_1
print(lista_final)

# año, gastos mensuales agua, gas, energia

año_2020 = [[12000, 35000, 10000], [50000, 45000, 15000], [15000, 20000, 50000], [100000, 30000, 65000], [50000, 45000, 150000], [65000, 200000, 30000]]
print(año_2020[1][0])
año_2020[3].insert(1,40000)
# año = [[gastos_enero],[gastos_febrero], [gastos_marzo], [gastos_abril], ... ]

# .extend   (agrega una dartos itrables)
# .pop      (Elimina un item de una lista por *el indice*)
# .remove   (Elimina un item de una lista por *el item en si*)


lista = ["hola", "to"]