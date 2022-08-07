nombre = input()
salario = int(input())

if salario <= 1000000:
    subsidio = 120000
else: 
    subsidio = 0
    
print("Nombre:", nombre)
print("Salario: ", salario)
print("Subcidio: ", subsidio)

