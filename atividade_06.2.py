import requests

# URL da API
url = 'https://randomuser.me/api/'

# Requisição GET
response = requests.get(url)

# Transformando em JSON
dados = response.json()

# Pegando informações
usuario = dados['results'][0]
nome = f"{usuario['name']['first']} {usuario['name']['last']}"
email = usuario['email']
pais = usuario['location']['country']

print(f"Nome: {nome}")
print(f"Email: {email}")
print(f"País: {pais}")
