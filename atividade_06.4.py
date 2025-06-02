import requests

# Entrada do código da moeda
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

# URL da API AwesomeAPI
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

# Requisição GET
response = requests.get(url)

# Transformando em JSON
dados = response.json()

chave = moeda + 'BRL'

if chave in dados:
    info = dados[chave]
    print(f"Moeda: {info['name']}")
    print(f"Valor atual: R$ {info['bid']}")
    print(f"Valor máximo: R$ {info['high']}")
    print(f"Valor mínimo: R$ {info['low']}")
    print(f"Última atualização: {info['create_date']}")
else:
    print("Moeda inválida ou não encontrada.")
