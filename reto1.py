codigo = int(input())
nombre = input()
cantidad = float(input())
valor = float(input())

valor_sin_iva = cantidad * valor
valor_final = valor_sin_iva + (valor_sin_iva * 0.19)

print(codigo)
print(nombre)
print(valor_sin_iva)
print(valor_final)
