import random
import string

# Entrada: quantidade de caracteres
quantidade = int(input("Informe a quantidade de caracteres para a senha: "))

# Conjunto de caracteres: letras, dígitos e caracteres especiais
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gerando a senha
senha = ''.join(random.choice(caracteres) for _ in range(quantidade))

print(f"Senha gerada: {senha}")
