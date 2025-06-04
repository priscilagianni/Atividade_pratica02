import csv

def escrever_csv(nome_arquivo, dados):
    colunas = ["Nome", "Idade", "Cidade"]

    with open(nome_arquivo, mode="w", newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso")


dados_pessoas = [
    {"Nome": "Luciana", "Idade": 30, "Cidade": "São Bernardo do Campo"},
    {"Nome": "Tayluan", "Idade": 20, "Cidade": "São João de Meriti"},
    {"Nome": "Priscila", "Idade": 26, "Cidade": "Pernambuco"}
]


escrever_csv("pessoas.csv", dados_pessoas)
