#sistema bancario

saldo = (int( ))
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Depositar \n[3] Saldo \n[0] sair: "))

    if opcao == 1:

        saque = int(input("digite o valor do saque: "))

        if saque > saldo:

            print("Erro: Saldo insuficiente para o saque.")

        else:
            saldo -= saque
            print(f"{saque} sacados da sua conta. Saldo restante: {saldo}")
            
    elif opcao == 2:

        deposito = int(input("digite o valor do deposito: "))

        saldo += deposito
        print(f"{deposito} depositados na sua conta. saldo atual: {saldo}")

    elif opcao == 3:
            print(f"{saldo} de saldo disponivel")
    else:
            print("obrigado por usar o sistema bancario, até logo!")
                    