import json 

list = []
n = int(input())

for i in range(n):
    list.append(input())

with open("lst.json", "w") as lst:
    json.dump(list, lst)

lst.close()

