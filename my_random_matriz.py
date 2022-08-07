import random
def int_validation(label):
    while True:
        try:
            num = int(int(input(label)))
            break
        except ValueError:
            print("Enter a integer value")
    return num

n_listas = random.randint(0, 10)
n_sublists = random.randint(0, 10)

list = []

odd_counters = 0
even_counters = 0

for i in range(n_listas):
    list.append([])
    for j in range(n_sublists):
        list[i].append(random.randint(0, 10))

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