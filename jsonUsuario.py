import json, requests
url = requests.get("https://jsonplaceholder.typicode.com/users") # ! Archivo json
text = url.text
data = json.loads(text)
user = data[int(input())]
print(f"Name: {user['name']}")
print(f"Phone: {user['phone']}")
print(f"Email: {user['email']}")
print(f"Address: {user['address']}")
# Posibilidad de agregar mas usuarios