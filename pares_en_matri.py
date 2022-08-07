def int_validation(label):
    while True:
        try:
            num = int(int(input(label)))
            break
        except ValueError:
            print("Enter a integer value")
    return num

n_listas = int(input("How many lists do you want:\n"))
n_sublists = int(input("How many sublists for each list do you want:\n"))

list = []

odd_counters = 0
even_counters = 0

for i in range(n_listas):
    list.append([])
    for j in range(n_sublists):
        num = int_validation(f"Agrege el elemento {j+1} de la lista {i+1}:\n")
        list[i].append(num)

print(list)
for i in range(len(list)):
    for j in range(n_sublists):
        if list[i][j] % 2 == 0:
            print(f"{list[i][j]} is even")
            even_counters += 1
        else:
            print(f"{list[i][j]} is odd")
            odd_counters += 1

print(f"Even: {even_counters}")
print(f"Odd: {odd_counters}")