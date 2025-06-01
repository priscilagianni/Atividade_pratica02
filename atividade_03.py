# Edn - atividade03.py

# --- 1. Classificador de Idade ---
def classificar_idade_interativo():
    """
    Solicita a idade do usuário e a classifica em categorias.
    """
    print("\n--- 1. Classificador de Idade ---")
    while True:
        try:
            idade_str = input("Por favor, digite sua idade: ")
            idade = int(idade_str)
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

    if 0 <= idade <= 12:
        classificacao = "Criança"
    elif 13 <= idade <= 17:
        classificacao = "Adolescente"
    elif 18 <= idade <= 59:
        classificacao = "Adulto"
    elif idade >= 60:
        classificacao = "Idoso"
    else: # Este caso não deve ser atingido com a validação acima, mas é um bom fallback
        classificacao = "Idade inválida"

    print(f"Com {idade} anos, você se classifica como: {classificacao}")

# --- 2. Calculadora de IMC ---
def calcular_imc_interativo():
    """
    Solicita peso e altura do usuário, calcula o IMC e classifica.
    """
    print("\n--- 2. Calculadora de IMC ---")
    while True:
        try:
            peso_str = input("Por favor, digite seu peso em kg (ex: 70.5): ")
            peso = float(peso_str)
            if peso <= 0:
                print("O peso deve ser um valor positivo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o peso.")

    while True:
        try:
            altura_str = input("Por favor, digite sua altura em metros (ex: 1.75): ")
            altura = float(altura_str)
            if altura <= 0:
                print("A altura deve ser um valor positivo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a altura.")

    imc = peso / (altura ** 2)
    classificacao = ""

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

# --- 3. Conversor de Temperatura ---
def converter_temperatura_interativo():
    """
    Solicita temperatura, unidade de origem e destino para conversão.
    """
    print("\n--- 3. Conversor de Temperatura ---")
    unidades_validas = {"C", "F", "K", "CELSIUS", "FAHRENHEIT", "KELVIN"}

    while True:
        try:
            temperatura_str = input("Digite a temperatura: ")
            temperatura = float(temperatura_str)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a temperatura.")

    while True:
        unidade_origem = input("Unidade de origem (C/Celsius, F/Fahrenheit, K/Kelvin): ").strip().upper()
        if unidade_origem in unidades_validas:
            # Padroniza para C, F ou K
            if "CELSIUS" in unidade_origem: unidade_origem = "C"
            elif "FAHRENHEIT" in unidade_origem: unidade_origem = "F"
            elif "KELVIN" in unidade_origem: unidade_origem = "K"
            break
        else:
            print("Unidade de origem inválida. Use C, F ou K.")

    while True:
        unidade_destino = input("Unidade para conversão (C/Celsius, F/Fahrenheit, K/Kelvin): ").strip().upper()
        if unidade_destino in unidades_validas:
            # Padroniza para C, F ou K
            if "CELSIUS" in unidade_destino: unidade_destino = "C"
            elif "FAHRENHEIT" in unidade_destino: unidade_destino = "F"
            elif "KELVIN" in unidade_destino: unidade_destino = "K"
            break
        else:
            print("Unidade de destino inválida. Use C, F ou K.")

    temp_convertida = None

    if unidade_origem == unidade_destino:
        temp_convertida = temperatura
    elif unidade_origem == "C":
        if unidade_destino == "F":
            temp_convertida = (temperatura * 9/5) + 32
        elif unidade_destino == "K":
            temp_convertida = temperatura + 273.15
    elif unidade_origem == "F":
        if unidade_destino == "C":
            temp_convertida = (temperatura - 32) * 5/9
        elif unidade_destino == "K":
            temp_convertida = (temperatura - 32) * 5/9 + 273.15
    elif unidade_origem == "K":
        if unidade_destino == "C":
            temp_convertida = temperatura - 273.15
        elif unidade_destino == "F":
            temp_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        print("Erro interno na lógica de conversão. Verifique as unidades.")
        return

    if temp_convertida is not None:
        print(f"{temperatura}°{unidade_origem} é equivalente a {temp_convertida:.2f}°{unidade_destino}")

# --- 4. Verificador de Ano Bissexto ---
def verificar_ano_bissexto_interativo():
    """
    Solicita um ano ao usuário e verifica se é bissexto.
    """
    print("\n--- 4. Verificador de Ano Bissexto ---")
    while True:
        try:
            ano_str = input("Digite um ano para verificar se é bissexto: ")
            ano = int(ano_str)
            if ano < 0:
                print("O ano não pode ser negativo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o ano.")

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} É bissexto.")
    else:
        print(f"O ano {ano} NÃO é bissexto.")

# --- Menu Principal de Execução ---
if __name__ == "__main__":
    print("Bem-vindo(a) às Atividades Práticas de Python!")
    print("Escolha qual atividade deseja executar:")

    while True:
        print("\n--- Menu ---")
        print("1. Classificador de Idade")
        print("2. Calculadora de IMC")
        print("3. Conversor de Temperatura")
        print("4. Verificador de Ano Bissexto")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ").strip()

        if escolha == '1':
            classificar_idade_interativo()
        elif escolha == '2':
            calcular_imc_interativo()
        elif escolha == '3':
            converter_temperatura_interativo()
        elif escolha == '4':
            verificar_ano_bissexto_interativo()
        elif escolha == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 0 e 4.")