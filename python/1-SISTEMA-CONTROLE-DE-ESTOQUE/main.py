# estoque inicial
import os
import time
from datetime import date

estoque = [
    {
        "codigo":"ce-001", 
        "nome": "cebola", 
        "quantidadeInicial": 100, 
        "estoqueAtual": 85, 
        "estoqueMinimo": 20, 
        "preco": 2.50},
    {"codigo": "to-002", "nome": "tomate", "quantidadeInicial": 80, "estoqueAtual": 45, "estoqueMinimo": 15, "preco": 3.80},
    {"codigo": "ba-003", "nome": "batata", "quantidadeInicial": 150, "estoqueAtual": 120, "estoqueMinimo": 30, "preco": 1.90},
    {"codigo": "al-004", "nome": "alho", "quantidadeInicial": 50, "estoqueAtual": 12, "estoqueMinimo": 10, "preco": 8.50},
    {"codigo": "ce-005", "nome": "cenoura", "quantidadeInicial": 70, "estoqueAtual": 65, "estoqueMinimo": 12, "preco": 2.20},
    {"codigo": "ma-006", "nome": "macarrão", "quantidadeInicial": 200, "estoqueAtual": 180, "estoqueMinimo": 40, "preco": 4.30},
    {"codigo": "ar-007", "nome": "arroz", "quantidadeInicial": 180, "estoqueAtual": 42, "estoqueMinimo": 35, "preco": 6.90},
    {"codigo": "fe-008", "nome": "feijão", "quantidadeInicial": 120, "estoqueAtual": 110, "estoqueMinimo": 25, "preco": 7.50},
    {"codigo": "ac-009", "nome": "açúcar", "quantidadeInicial": 90, "estoqueAtual": 15, "estoqueMinimo": 18, "preco": 3.20},
    {"codigo": "sa-010", "nome": "sal", "quantidadeInicial": 60, "estoqueAtual": 55, "estoqueMinimo": 8, "preco": 1.50}
]

def alerta():
    input("APERTE EM QUALQUER TECLA PARA CONTINUAR...")

def tituloDoSistema(titulo):
    print("=" * len(titulo))
    print(titulo)
    print("=" * len(titulo))


# MENU DO SISTEMA
def menuDoSistema(itensdoMenu):
    tituloDoSistema("SISTEMA - CONTROLE DE ESTOQUE")
    for index, opcao in enumerate(itensdoMenu, start=1):
        print(f"{index} - {opcao}")


def cadastrarProduto(estoque):
     while True:
        tituloDoSistema("Cadastrar Produto")
        codigo = input("Digite o codigo do produto: ")
        for produtos in estoque:
            if produtos["codigo"] == codigo:
                print("Esse codigo já está em uso em um outro produto")
                while True:
                    codigo = input("Digite o codigo do produto: ")
                    for produtos in estoque:
                        if produtos["codigo"] == codigo:
                            print("Esse codigo já está em uso em um outro produto")
                        break
                    break


        nome = input("Digite o nome do produto: ")
        quantidadeinical = int(input("Quantidade inicial do produto em estoque: "))
        estoqueMinimo = int(input("Estoque minimo do produto: "))
        if quantidadeinical < 0 and estoqueMinimo < 0:
            while True:
                print("Digite o quantidade inicial do produto em estoque maior ou igual a zero: ")
                print("Digitte a quantidade inicial do produto maior ou igual a zero: ")
                quantidadeinical = int(input("Quantidade inicial do produto em estoque: "))
                estoqueMinimo = int(input("Estoque minimo do produto: "))
                if quantidadeinical < 0 and estoqueMinimo < 0:
                    continue
                break
        preco = int(input("Qal o preco do produto: "))



        produto = {
                    "codigo": codigo,
                    "nome": nome,
                    "quantidadeInicial": quantidadeinical,
                    "estoqueAtual":quantidadeinical,
                    "estoqueMinimo": estoqueMinimo,
                    "preco":preco
                }
        estoque.append(produto)

        op = input("deseja cadastrar mais produtos ? [S/N]")
        if op in "Ss":
            continue
        print("produtos cadastrados: ")
        print(estoque)
        break

def consultarestoque(estoque):
    os.system("cls")
    menuDoSistema(['Listar todos os produtos com estoque', 'Pesquisar produto por código','Destacar produtos com estoque abaixo do mínimo', 'Calcular valor total do estoque'])
    op = input("escolha uma opção: ")
    if op == "1":
        os.system("cls")
        print("\n" + "="*85)
        print("LISTA DE PRODUTOS")
        print("="*85)
        print(f"{'Código':<10} {'Nome':<15} {'Quantidade':<12}  {'Atual':<10}  {'Estoque Mínimo':<15} {'Status':<15}")
        print("-"*85)
        for produto in estoque:
            status = "🟢 NORMAL" if produto['estoqueAtual'] > produto['estoqueMinimo'] else "🔴 BAIXO"
            if produto['estoqueAtual'] < produto['estoqueMinimo']:
                status = "🔴 BAIXO"
            elif produto['estoqueAtual'] <= produto['estoqueMinimo'] * 1.5:
                status = "🟡 ALERTA"
            else:
                status = "🟢 NORMAL"
                
            print(f"{produto['codigo']:<10} {produto['nome']:<15} {produto['quantidadeInicial']:<15} {produto['estoqueAtual']:<13} {produto['estoqueMinimo']:<13} {status:<15}")
            time.sleep(.5)
        alerta()
        os.system("cls")
    elif op == "2":
        os.system("cls")
        print("\n" + "="*85)
        print("LISTA DE PRODUTOS")
        print("="*85)
        codigo = input("Digite o codigo do produto: ")
        os.system("cls")
        print("\n" + "="*85)
        print("LISTA DE PRODUTOS")
        print("="*85)
        print(f"{'Código':<10} {'Nome':<15} {'Quantidade':<12}  {'Atual':<10}  {'Estoque Mínimo':<15} {'Status':<15}")
        print("-"*85)

        for produto in estoque:
            if(produto['codigo'] == codigo):     
                status = "🟢 NORMAL" if produto['estoqueAtual'] > produto['estoqueMinimo'] else "🔴 BAIXO"
                if produto['estoqueAtual'] < produto['estoqueMinimo']:
                    status = "🔴 BAIXO"
                elif produto['estoqueAtual'] <= produto['estoqueMinimo'] * 1.5:
                    status = "🟡 ALERTA"
                else:
                    status = "🟢 NORMAL"
                print(f"{produto['codigo']:<10} {produto['nome']:<15} {produto['quantidadeInicial']:<15} {produto['estoqueAtual']:<13} {produto['estoqueMinimo']:<13} {status:<15}")
                alerta()
                break
            else: 
                print("PRODUTO NÃO ENCONTRADO...")
                time.sleep(2)
                break
        os.system("cls")
    elif op == "3":
        os.system("cls")
        print("\n" + "="*85)
        print("LISTA DE PRODUTOS EM BAIXA NO ESTOQUE.")
        print("="*85)
        print(f"{'Código':<10} {'Nome':<15} {'Quantidade':<12}  {'Atual':<10}  {'Estoque Mínimo':<15} {'Status':<15}")
        print("-"*85)
        
        for produto in estoque:
            if produto['estoqueAtual'] < produto['estoqueMinimo']:
                status = "🔴 BAIXO"
                print(f"{produto['codigo']:<10} {produto['nome']:<15} {produto['quantidadeInicial']:<15} {produto['estoqueAtual']:<13} {produto['estoqueMinimo']:<13} {status:<15}")
        alerta()
    elif op == "4":
        os.system("cls")
        print("\n" + "="*85)
        print("CALCUAR O VALOR TOTAL DO ESTOQUE.")
        print("="*85)
        total = 0 
        for produto in estoque:
            totoalProduto = produto['preco'] * produto['estoqueAtual']
            total += totoalProduto
        print(f"valor atual do estoque: {total}-R$")
        alerta()
        os.system("cls")
            
                
            
def registroDeEntrada(estoque):   
    codigoProduto = input("Digite o codigo do produto: ")

    for produto in estoque:
        if(produto['codigo'] == codigoProduto):
            quantidadeProduto = int(input("Informe a quantidade de produto: "))
            if(quantidadeProduto > 0 ):
                produto['estoqueAtual'] += quantidadeProduto
            else:
                print("A quantidade de produto deve ser maior que 0.")
            break
            

def registraSaida(estoque):
    codigoProduto = input("Qual o codigo do produto: ")
    for produto in estoque:
        if produto['codigo'] == codigoProduto:
            if produto['estoqueAtual'] > produto['estoqueMinimo']:
                saidaProduto = int(input("Qual a quantidade de saida: "))
                if(saidaProduto > 0 ):
                    produto['estoqueAtual'] -= saidaProduto
                else:
                    print("o sistema não pode realizar retirada de produtos menor ou igual a zero.")
        break        
        
                
       
                

def main():
    while True:
        menuDoSistema(['Cadastrar Produto', 'Consultar Estoque', 'Resgistrar Entrada', 'Registrar Saida','Sair'])
        op = input("Escolha uma opção valida: ")
        if op == "1":
            cadastrarProduto(estoque)
            os.system("cls")
        elif op == "2":
            consultarestoque(estoque)
        elif op == "3":
            registroDeEntrada(estoque)
        elif op == "4":
            registraSaida(estoque)
        elif op == "5":
            break
        else:
            print("opção invalida...")
            
        
            


if __name__ == "__main__":
    main()
