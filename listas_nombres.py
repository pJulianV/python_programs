# Dada una lista con nombres completos de personas, realizar un programa que
# genere una segunda con la cantidad de palabras de cada uno de los nombres. La
# lista de nombres debe llenarse a través de nombres que se ingresan por teclado,
# hasta que el nombre ingresado sea “FIN”
# Se debe imprimir la lista de nombres y la lista con la cantidad de palabras de cada
# nombre.


print("Usted ingresara una cantidad indefinida de nombres, para terminar escriba FIN")

def lst_nombres():
    i = 0
    nombres = []
    c_palabras = []
    nombre = ""
    while nombre.upper() != "FIN":
        i += 1
        nombre = input(f"{i} Escriba un nombre: ")
        nombres.append(nombre)
        c_palabras.append(len(nombre.split()))
    return nombres, c_palabras

print(lst_nombres())