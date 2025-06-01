#EdN - Atividade prática 04.py

# --- 1. Calculadora de Operações Básicas ---
def calculadora_basica():
    """
    Desenvolve uma calculadora que realiza as quatro operações básicas.
    Solicita dois números e a operação, trata erros e mostra o resultado.
    """
    print("\n--- 1. Calculadora de Operações Básicas ---")
    num1 = None
    num2 = None
    operacao = ""

    # Solicita o primeiro número
    while num1 is None:
        try:
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Solicita o segundo número
    while num2 is None:
        try:
            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Solicita a operação e tenta realizá-la
    while True:
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        resultado = None

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida. Tente novamente com outra operação ou números.")
                continue # Continua o loop para pedir outra operação
            else:
                resultado = num1 / num2
        else:
            print("Operação inválida. Por favor, digite +, -, * ou /.")
            continue # Continua o loop para pedir outra operação

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado:.2f}")
        break # Sai do loop se a operação for válida e bem-sucedida

# --- 2. Registro de Notas da Turma ---
def registrar_notas_turma():
    """
    Programa para o professor registrar as notas da turma.
    Calcula a média, aceita apenas notas entre 0 e 10, e ignora inválidas.
    """
    print("\n--- 2. Registro de Notas da Turma ---")
    notas = []
    print("Digite as notas da turma (entre 0 e 10). Digite 'fim' para encerrar.")

    while True:
        entrada = input("Digite a nota ou 'fim': ").strip().lower()
        if entrada == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nNotas registradas: {notas}")
        print(f"A média da turma é: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

# --- 3. Verificador de Senha Forte ---
def verificar_senha_forte():
    """
    Verifica se a senha é forte (pelo menos 8 caracteres e pelo menos um número).
    Continua pedindo até que uma válida seja inserida ou o usuário digite 'sair'.
    """
    print("\n--- 3. Verificador de Senha Forte ---")
    while True:
        senha = input("Digite uma senha (min. 8 caracteres, com número, ou 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            print("Saindo do verificador de senha.")
            break

        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.")
            continue

        tem_numero = False
        for char in senha:
            if char.isdigit():
                tem_numero = True
                break

        if not tem_numero:
            print("Senha fraca: deve conter pelo menos um número.")
            continue

        print("Senha forte! Senha aceita.")
        break

# --- 4. Verificador de Par ou Ímpar ---
def verificar_par_impar():
    """
    Solicita números inteiros ao usuário, informando se são pares ou ímpares.
    Conta o total de pares e ímpares.
    """
    print("\n--- 4. Verificador de Par ou Ímpar ---")
    total_pares = 0
    total_impares = 0
    print("Digite números inteiros. Digite 'fim' para encerrar.")

    while True:
        entrada = input("Digite um número inteiro ou 'fim': ").strip().lower()
        if entrada == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                total_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                total_impares += 1
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

    print(f"\n--- Resumo ---")
    print(f"Total de números pares: {total_pares}")
    print(f"Total de números ímpares: {total_impares}")

# --- Menu Principal de Execução ---
if __name__ == "__main__":
    print("Bem-vindo(a) às Novas Atividades Práticas de Python!")
    print("Escolha qual programa deseja executar:")

    while True:
        print("\n--- Menu ---")
        print("1. Calculadora de Operações Básicas")
        print("2. Registro de Notas da Turma")
        print("3. Verificador de Senha Forte")
        print("4. Verificador de Par ou Ímpar")
        print("0. Sair")

        escolha = input("Digite o número da opção desejada: ").strip()

        if escolha == '1':
            calculadora_basica()
        elif escolha == '2':
            registrar_notas_turma()
        elif escolha == '3':
            verificar_senha_forte()
        elif escolha == '4':
            verificar_par_impar()
        elif escolha == '0':
            print("Saindo dos programas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 0 e 4.")
            