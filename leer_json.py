import json

with open("diccionario.json", "r") as archivo:
    diccionario = json.load(archivo)

print(diccionario)

archivo.close()

print(diccionario)

n_letras = int(input())
n = (input)
print(diccionario[n])



with open("lst.json", "r") as archivo:
    lst = json.load(archivo)

print(lst)

archivo.close()

print(lst)

for i in range(len(lst)):
    print(f"{i+1}: {lst[i]}")