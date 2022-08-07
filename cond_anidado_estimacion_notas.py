nombre = input()
eva_cuantitativa = int(input())

if eva_cuantitativa <= 59:
    eva_cualitativa = "D"
else:
    if eva_cuantitativa <= 79:
        eva_cualitativa = "C"
    else:
        if eva_cuantitativa <= 89:
            eva_cualitativa = "B"
        else:
            if eva_cuantitativa <= 100:
                eva_cualitativa = "A"
            else: 
                print("Intente de nuevo e igrese un valor valido")

print(nombre)
print(eva_cuantitativa)
print(eva_cualitativa)
























# nombre = input()
# eva_cuantitativa = int(input())

if eva_cuantitativa <= 59:
    eva_cualitativa = "D"
elif eva_cuantitativa <= 79:
        eva_cualitativa = "C"
elif eva_cuantitativa <= 89:
        eva_cualitativa = "B"
elif eva_cuantitativa <= 100:
        eva_cualitativa = "A"
else: 
    print("Intente de nuevo e igrese un valor valido") 
