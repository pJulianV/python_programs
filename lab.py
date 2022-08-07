# n Dados de n caras
import random


def dados(n_dados):
    i = 0
    sum = 0
    while i < n_dados:
        i += 1
        random_n = random.randint(0, int(input(f"¿Cuantas caras tiene el dado {i}?\n")))
        print(f"Dado {i} saco un {random_n}")
        sum = sum + random_n
    return sum

# print("Total:", dados(int(input("Cuantas dados quieres tirar: "))))

def comision():
    nombre = input("Ingrese nombre del conductor: ")
    placa = input("Ingrese placa: ")
    v_pasaje = float(input("Ingrese valor del pasaje: "))
    v_encomiendas = float(input("Ingrese valor encomiendas"))

    c_pasaje = v_pasaje * 0.25
    c_encomienda = v_pasaje * 0.15

    print("Nombre:", nombre)
    print("Placa:", placa)

    # v_pasaje ="{:,.3f}".format(v_pasaje )

    print("Valor del pasaje:","{:,.3f}".format(v_pasaje ))
    # .format => <class "str">

    print("Valor encomienda", round(v_encomiendas, 2))
    # round => <class "float">

    print("Comision pasaje:", c_pasaje, "\nComision encomienda: ", c_encomienda)
    print(f"Comision total: {c_pasaje + c_encomienda}")