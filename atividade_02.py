# Atividade prática 02 Escola da nuvem

print("--- Questão 1: Conversor de Moeda ---")

valor_reais_ativ1 = 100.00
taxa_dolar_ativ1 = 5.20
taxa_euro_ativ1 = 6.15

valor_dolar_ativ1 = valor_reais_ativ1 / taxa_dolar_ativ1
valor_euro_ativ1 = valor_reais_ativ1 / taxa_euro_ativ1

print(f"Valor em Reais: R$ {valor_reais_ativ1:.2f}")
print(f"Taxa do Dólar: R$ {taxa_dolar_ativ1:.2f}")
print(f"Taxa do Euro: R$ {taxa_euro_ativ1:.2f}")
print(f"R$ {valor_reais_ativ1:.2f} equivalem a US$ {valor_dolar_ativ1:.2f}")
print(f"R$ {valor_reais_ativ1:.2f} equivalem a € {valor_euro_ativ1:.2f}")

print("\n" + "="*40 + "\n")

print("--- Questão 2: Calculadora de Desconto ---")

nome_produto_ativ2 = "Camiseta"
preco_original_ativ2 = 50.00
porcentagem_desconto_ativ2 = 20

valor_desconto_ativ2 = preco_original_ativ2 * (porcentagem_desconto_ativ2 / 100)
preco_final_ativ2 = preco_original_ativ2 - valor_desconto_ativ2

print(f"Nome do Produto: {nome_produto_ativ2}")
print(f"Preço Original: R$ {preco_original_ativ2:.2f}")
print(f"Porcentagem de Desconto: {porcentagem_desconto_ativ2}%")
print(f"Valor do Desconto: R$ {valor_desconto_ativ2:.2f}")
print(f"Preço Final: R$ {preco_final_ativ2:.2f}")

print("\n" + "="*40 + "\n")

print("--- Questão 3: Calculadora de Média Escolar ---")

nota1_ativ3 = 7.5
nota2_ativ3 = 8.0
nota3_ativ3 = 6.5

media_final_ativ3 = (nota1_ativ3 + nota2_ativ3 + nota3_ativ3) / 3

print(f"Nota 1: {nota1_ativ3:.1f}")
print(f"Nota 2: {nota2_ativ3:.1f}")
print(f"Nota 3: {nota3_ativ3:.1f}")
print(f"Média Final: {media_final_ativ3:.2f}")

print("\n" + "="*40 + "\n")

print("--- Questão 4: Calculadora de Consumo de Combustível ---")

distancia_ativ4 = 300
combustivel_ativ4 = 25

consumo_medio_ativ4 = distancia_ativ4 / combustivel_ativ4

print(f"Distância Percorrida: {distancia_ativ4} km")
print(f"Combustível Gasto: {combustivel_ativ4} litros")
print(f"Consumo Médio: {consumo_medio_ativ4:.2f} km/l")

print("\n" + "="*40 + "\n")