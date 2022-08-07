equilatero = 0
isoceles = 0
escaleno = 0

n_triangulos = int(int(input()))

for i in range(n_triangulos):
    lado1 = int(input("Lados"))
    lado2 = int(input("Lados"))
    lado3 = int(input("Lados"))

    if lado1 == lado2 and lado2 == lado3:
        equilatero += 1
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        isoceles += 1
    else:
        escaleno += 1
        
print(n_triangulos)
print(equilatero)
print(isoceles)
print(escaleno)