from cmath import pi
import random

# Area Circunferencia

def area_circunferencia(r):
    r = int(input("Inserta radio: "))
    return "{:,.2f}".format(pi * (r**2))

# Calificaciones

def calificaciones(n1, n2, n3, n4, n5, nI):
    n1 = float(input("Inserte nota Reto 1 (10%):\n"))
    n2 = float(input("Inserte nota Reto 2 (10%):\n"))
    n3 = float(input("Inserte nota Reto 3 (20%):\n"))
    n4 = float(input("Inserte nota Reto 4 (20%):\n"))
    n5 = float(input("Inserte nota Reto 5 (20%):\n"))
    nI = float(input("Inserte nota Ingles (20%):\n"))
    return n1 * 0.1 + n2 * 0.1 + n3 * 0.2 + n4 * 0.2 + n5 * 0.2 + nI * 0.2 #round o .format en indx

# Area de un Triangulo

def area_triangulo(base, altura):
    return (base * altura) / 2


# Digitos de pi 

def digitos_pi():
    digitos = int(input("Cuanto digitos de pi despues de la (,) quiere ver?"))
    return round(pi, digitos)


# Area de un triangulo
def area_triangulo():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = "{:,.2f}".format((base * altura / 2 ) )
    print(area) #str


# IVA n% 
def n_iva():
    porc_iva = float(input("Ingrese un valor de 0 a 100 para el porcentaje del iva"))
    valor_unit = float(input("Ingrese Valor: "))
    cantidad = float(input("Ingrese cantidad: "))

    valor_producto = valor_unit * cantidad
    iva = valor_producto * 0.19
    valor_producto_iva = valor_producto + iva

    print("El valor (sin iva) del producto es de","{:,.2f}".format(valor_producto))
    print("El iva es de","{:,.2f}".format(iva))
    print("El valor (con iva) del producto","{:,.2f}".format(valor_producto_iva))


# Comision Conductor
def comision():
    nombre = input("Ingrese nombre del conductor: ")
    placa = input("Ingrese placa: ")
    v_pasaje = float(input("Ingrese valor del pasaje: "))
    v_encomiendas = float(input("Ingrese valor encomiendas"))

    c_pasaje = v_pasaje * 0.25
    c_encomienda = v_pasaje * 0.15

    print("Nombre:", nombre)
    print("Placa:", placa)

    v_pasaje ="{:,.2f}".format(v_pasaje )

    print("Valor del pasaje:","{:,.2f}".format(v_pasaje ))
    # .format => <class "str">

    print("Valor encomienda", round(v_encomiendas, 2))
    # round => <class "float">

    print("Comision pasaje:", c_pasaje, "\nComision encomienda: ", c_encomienda)
    print(f"Comision total: {c_pasaje + c_encomienda}") 


# Generador de contraseñas
def generador_psw(lenght_pswd ):
    letras = "qwertyuiopaasdfghjklñzxcvbnm"
    numeros = "1234567890" 
    simbolos = "|°!#$%&/()='?¿¡\,;.:-_{[^+*´¨"
    lenght_pswd = int(input("Cuantos digitos va a tener su contraseña"))
    pswd = "".join(random.sample(letras, numeros, simbolos))

# Dados

def dados(n_dados):
    i = 0
    sum = 0
    while i < n_dados:
        i += 1
        random_n = random.randint(0, int(input(f"¿Cuantas caras tiene el dado {i}?\n")))
        print(f"Dado {i} saco un {random_n}")
        sum = sum + random_n
    return sum

print("Total:", dados(int(input("Cuantas dados quieres tirar: "))))