import requests

# Entrada do CEP
cep = input("Digite o CEP (apenas números): ")

# URL da API ViaCEP
url = f"https://viacep.com.br/ws/{cep}/json/"

# Requisição GET
response = requests.get(url)

# Transformando em JSON
endereco = response.json()

if 'erro' in endereco:
    print("CEP inválido.")
else:
    logradouro = endereco['logradouro']
    bairro = endereco['bairro']
    cidade = endereco['localidade']
    estado = endereco['uf']

    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")
