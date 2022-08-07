# Programa de listas dentro de listas
# Posición de los datos



import random
numeros = []
rows = random.randint(0, 9)
cols = random.randint(0, 9)



for i in range(rows):
    numeros.append([])
    for j in range(cols):
        numeros[i].append(int(random.randint(0, 9)))



# Imprimir lista dentro de la lista matriz
print(numeros,'\n')


num = int(input())
# Procesar lista dentro de la lista matriz
for i in range(rows):
    for j in range(cols):
        if num is numeros[i][j]:
            print(numeros[i][j]," en la posición [",i,"],[",j,"]") # Terminar 
