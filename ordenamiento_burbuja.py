def ordenamiento_burbuja(n, lista):
    for i in range(n-1):
        print(f"Elemento {i} es {lista[i]}")
        for j in range(i+1, n):
            print(f"Elemento {j} es {lista[j]}")
            if lista[i]>lista[j]:
                print("----------------------------------------------------------------")
                print(f"{lista[i]} es \"mayor\" que {lista[j]}")
                # ! Intercambio de lugar
                t = lista[i]
                print(f"Temporal es {lista[i]}")
                lista[i] = lista[j] 
                print(f"Elemento {i} ahora es {lista[j]}")
                lista[j] = t
                print(f"Ahora el elemento {j} es {lista[j]}")
                print("----------------------------------------------------------------")
                print(lista)
                print("----------------------------------------------------------------")


lista = ["pan", "harina", "arroz", "telefono", "television", "jabon"]
n = len(lista)

ordenamiento_burbuja(n, lista)

print(lista)