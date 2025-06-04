import csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 28, "São Paulo"],
    ["Ribeiro", 25, "Rio de Janeiro"],
    ["Monteiro", 25, "Rio de Janeiro"]
]

# Escrevendo no CSV
with open("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

# Lendo e organizando os dados
with open("dados.csv", mode="r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

cabecalho = linhas[0].strip()

nomes = []

for linha in linhas[1:]:
    nomes.append(linha.strip())

print(cabecalho)

for nome in nomes:
    print(nome)

   
    
