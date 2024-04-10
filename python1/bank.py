# -*- coding: cp1252 -*-
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do dep�sito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Dep�sito: R$ {valor:.2f}\n"

        else:
            print("Falha na opera��o! O valor informado � inv�lido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na Opera��o! Voc� n�o tem saldo suficiente")

        elif excedeu_limite:
            print("Falha da Opera��o! O valor do saque excede o limite")

        elif excedeu_saques:
            print("Falha na Opera��o! N�mero m�ximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na Operra��o! O valor informado � inv�lido")

    elif opcao == "e":
        print("===============EXTRATO===============")
        print("N�o foram realizadas movimenta��es." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "q":
        break

    else:
        print("Opera��o inv�lida, por favor selecione novamente a op��o desejada.")


