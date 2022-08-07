from io import open
import os
from unittest.mock import patch

n = int(input("Escriba 1 para sobreescribir datos (cualquier otro numero para continuar con datos actuales): "))
if n == 1:
    archivo = open("archivo.txt", "w")
    n = int(input())
    for i in range(n):
        
        nom = input()
        if i == n-1:
            archivo.write(f"{nom}")
        else:
            archivo.write(f"{nom}\n")

archivo = open("archivo.txt", "a")

n = int(input())
for i in range(n):
    nom = input()
    archivo.write(f"\n{nom}")

archivo = open("archivo.txt", "r")
print(archivo.read())

archivo = open("archivo.txt", "r")
lista_nombres = archivo.readlines()

archivo.close()

print(lista_nombres)

for i in range(len(lista_nombres)):
    print(f"{i+1}: {lista_nombres[i]}")