import datetime

def obter_categoria(saldo):
    if saldo >= 5000:
        return "Ouro"
    elif saldo >= 2000:
        return "Prata"
    else:
        return "Bronze"

while True:
    opcao = input("Digite a opção desejada (d para depósito, s para saque, e para extrato, q para sair): ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            extrato += f"[{data}] Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            extrato += f"[{data}] Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "e":
        categoria = obter_categoria(saldo)
        print("\n================ EXTRATO ================")
        print(f"Categoria do cliente: {categoria}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Opção inválida! Por favor, digite uma opção válida.") 