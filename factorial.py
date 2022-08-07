def int_validator(label):
    while True:
        try:
            data = int(input(label))
            break
        except ValueError:
            print("Enter a integer value")
    return data

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1) # ! No lo copies intentalo tu
    # ! En la misma funcion esta el ciclo
# *    n = 3
# *    recursive_factorial(3)
# *    3 * recursive_factorial(2)
# *    2 * recursive_factorial(1)
# *    3 * 2 * 1



def factorial(n):
    if n == 0 or n == 1:
        print(f"{n} es 1")
        return 1
    else:
        f = 1
        for i in range(n, 1, -1):
            f = f * i
            print(f)
    return f


n = int_validator("Enter number: ")
print(f"The {n} factorial is {recursive_factorial(n)}")