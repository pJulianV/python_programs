def retorna_lista(var_lista, var_num, var_lista1):
    return var_lista + [var_num] + var_lista


lista = retorna_lista([1, 4,2,1,6], 3, [1,5,2,1])
print(type(lista))
print(lista)
