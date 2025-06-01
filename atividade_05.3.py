from datetime import date

def calcular_idade_em_dias():
  print("Para calcular sua idade em dias, preciso de algumas informações:")
  dia_nascimento = int(input("Qual o dia do seu nascimento (ex: 15)? "))
  mes_nascimento = int(input("Qual o mês do seu nascimento (ex: 8 para agosto)? "))
  ano_nascimento = int(input("Qual o ano do seu nascimento (ex: 1990)? "))
  
  data_atual = date.today()
  data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento) 
  
  diferenca = data_atual - data_nascimento
  return diferenca.days

result = calcular_idade_em_dias()
print(f"A idade da pessoa em dias é: {result} dias.")