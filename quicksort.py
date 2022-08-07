import random
def particion(arr):
    p = arr[0]
    mayores = []
    menores = []
    for i in range(1, len(arr)):
        if arr[i] > p:
            mayores.append(arr[i])
        else:
            menores.append(arr[i])
    return menores, p, mayores

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        menores, p, mayores = particion(arr)
        return quicksort(menores) + [p] + quicksort(mayores)

n = random.randint(1,10000)
arr = []
for i in range(n):
    arr.append(random.randint(1,1000))
    arr.append(random.randint(1, 1000))
print(arr)

print(quicksort(arr))