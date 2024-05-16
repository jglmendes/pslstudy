#Bootcamp DIO - Sistema Bancário
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==>  """

saldo = 0
limite = 500
entradas = []
saidas = []
qtd_saques = 0
LIMITE_SAQUE = 3

def exibir_extrato(saldo, entradas, saidas):
    extrato = f"""
    Extrato:
    Entradas: {entradas}
    Saídas: {saidas}
    Saldo: R${saldo:.2f}
    """
    print(extrato)

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        print("Inicializando a operação de Depósito: ")
        while True:
            try:
                deposito = float(input("Insira o valor a ser depositado em conta ou [-1] para encerrar: "))
                if deposito == -1:
                    break
                elif deposito > 0:
                    saldo += deposito
                    entradas.append(deposito)
                    print(f"Depósito de R${deposito:.2f} realizado com sucesso. Saldo atual: R${saldo:.2f}.")
                else:
                    print("Valor Inválido. Favor inserir valores positivos.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

    elif opcao == "s":
        print("Inicializando a operação de Saque: ")
        while qtd_saques < LIMITE_SAQUE:
            try:
                saque = float(input("Insira o valor a ser sacado ou [-1] para encerrar: "))
                if saque == -1:
                    break
                elif saque > 0:
                    if saque <= limite and saque <= saldo:
                        saldo -= saque
                        saidas.append(saque)
                        qtd_saques += 1
                        print(f"Saque de R${saque:.2f} efetuado com sucesso. Saldo atual: R${saldo:.2f}.")
                        if qtd_saques == LIMITE_SAQUE:
                            print("Limite de saques diários atingido.")
                    else:
                        print("Valor de saque acima dos limites ou saldo insuficiente.")
                else:
                    print("Valor Inválido. Favor inserir valores positivos.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

    elif opcao == "e":
        exibir_extrato(saldo, entradas, saidas)

    elif opcao == "q":
        print("Encerrando o sistema bancário. Obrigado por utilizar nossos serviços.")
        break

    else:
        print("\nOperação Inválida, por favor selecione novamente a operação desejada.")
