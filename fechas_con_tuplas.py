def cargar_fecha():
    dd = int(input("Ingrese numero de dia: "))
    mm = int(input("Ingrese numero de mes: "))
    aa = int(input("Ingrese numero de año: "))
    return (dd, mm, aa)


fecha = cargar_fecha()


def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")


imprimir_fecha(fecha)
