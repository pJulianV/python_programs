def int_validation(label):
    while True:
        try:
            data = int(input(label))
            break
        except ValueError:
            print(f"{label} No es valido")
    return data


def code_validation(label,nombres):
    while True:
        try:
            data = int(int(input(label)))
            print(nombres.get(data, "ERROR"))
            if nombres.get(data, "ERROR") == "ERROR":  # ? ERROR palabra reservada
                print(data, nombres.get(data, "ERROR"))
                continue
            break
        except ValueError:
            print("Enter a valid code: ")
    return data


def cal_valor_product(cantidad, valor):
    return cantidad * valor

# ! def add_product_validation(label):
# !     return
# ! if add_product_validation(" ")
