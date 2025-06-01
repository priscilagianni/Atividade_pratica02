def calcular_gorjeta():
  valor_conta = float(input("Qual o valor total da conta? R$"))
  porcentagem_gorjeta = float(input("Qual a porcentagem de gorjeta desejada (ex: 15 para 15%)? "))
  
  valor_gorjeta = valor_conta * (porcentagem_gorjeta / 100)
  return valor_gorjeta # Agora retorna o valor
  
result = calcular_gorjeta()  

print(result)