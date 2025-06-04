import json

dados = {
        "nome": "Ana", 
        "Idade": 28,
        "Cidade": "São Paulo"
    } 

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)