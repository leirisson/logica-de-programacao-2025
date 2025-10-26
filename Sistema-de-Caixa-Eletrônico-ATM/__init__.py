

saldoConta = 5000
contTentativadaSenha = 0

def mensagem(titulo):
    print("="* len(titulo))
    print(f"{titulo}")
    print("=" * len(titulo))

def extrato(saldo):
    mensagem("Sistema de Caixa Eletrônico (ATM)")
    mensagem("EXTRATO DA CONTA")
    print("Saldo: ",saldo)


def menuSistemaDeCaixa():
    print("1: Verificar extrado da conta")
    print("2: Realizar saque")
    print("3: Sair")

def login(contTentativadaSenha, saldoConta):
    pincorreto = "123456"

    while True:

        mensagem("Sistema de Caixa Eletrônico (ATM)")
        pinUsuario = (input("Digite o código PIN do seu cartão: "))

        if pinUsuario not in pincorreto:
            contTentativadaSenha +=1
            print(f"Senha incorreta, você trerá mais 3 tentativas.")
        print(f"tentativa: {contTentativadaSenha}")

        if(contTentativadaSenha == 3):
            print("números de tentativa esgotada conta bloqueada.")
            break
        elif pinUsuario == pincorreto:
            mensagem("Sistema de Caixa Eletrônico (ATM)")
            menuSistemaDeCaixa()
            op = input("escolha sua opção: ")
            if (op == "1"):
                extrato(saldoConta)
            elif (op == "2"):
                valorSaque = int(input("informe o valor do saldo: "))
                if(valorSaque > saldoConta):
                    print("Seu saque não pode ser maior que o valor do saldo.")
                else:
                    saldoConta = saldoConta - valorSaque
                    print("Saque realizado com sucesso.")
                    print(f"saldo atual da conta: {saldoConta}")
            elif (op == "3"):
                print("Sair")
                break
            else:
                print("opção incorreta")


login(contTentativadaSenha, saldoConta)

