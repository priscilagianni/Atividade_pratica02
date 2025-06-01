import re

def verificar_palindromo():
  texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

  if texto.strip() == "": 
    return "Escreva algo"
    
  texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
  
  if texto_limpo == texto_limpo[::-1]:
    return "Sim"
  else:
    return "Não"

result = verificar_palindromo()
print(result)