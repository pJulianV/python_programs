import mod_dict_n_shop
n = mod_dict_n_shop.int_validation("Enter number of articles what do you want to add: ")

# ! Guardar los nombres y valores en un archivo para reutilizarse

nombres = {}
valores = {}
valor_compra = 0

for i in range(n):
    nombres[i+1] = input("Nombre: ")
    valores[i+1] = mod_dict_n_shop.int_validation("Valor: ")
    print(nombres.get(i+1))
    print(valores.get(i+1))

print(nombres)
print(valores)

n = mod_dict_n_shop.int_validation("Enter number of articles what do you want to buy: ")

for i in range(n):
    codigo = mod_dict_n_shop.code_validation("Codigo: ",nombres)
    cantidad = mod_dict_n_shop.int_validation("Cantidad: ")
    valor_producto = mod_dict_n_shop.cal_valor_product(cantidad, valores.get(codigo))
    valor_compra += valor_producto
    print(valores.get(codigo))
    print(nombres.get(codigo))
    print(valor_producto)
    print(cantidad)

print("Do you want to add or buy any products? a => add, b => buy, c => cancel")

print(valor_compra) # purchase
print(nombres)
print(valores)