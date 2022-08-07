#Llenar la lista dentro de lista (Matriz)
numeros=[]
for i in range(3):
    numeros.append([])
    for j in range(3):
        numeros[i].append(int(input("Número: ")))
        #Imprimir la lista dentro de lista (Matriz)
print(numeros)
        #Procesar lista dentro de lista
cpares=0
cimpares=0
for i in range(3):
    for j in range(3):
        if numeros[i][j]%2==0:
            cpares+=1
        else:
            cimpares+=1
print("La Cantidad de Pares es: ",cpares)
print("La Cantidad de Impares es: ",cimpares)