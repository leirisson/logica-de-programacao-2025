# estoque inicial
import os

estoque = [{"codigo": "ce-001", "nome": "cebola", "quantidadeinical": 100, "estoqueMinimo": 20}]


def tituloDoSistema(titulo):
    print("=" * len(titulo))
    print(titulo)
    print("=" * len(titulo))


# MENU DO SISTEMA
def menuDoSistema():
    tituloDoSistema("SISTEMA - CONTROLE DE ESTOQUE")
    opcaoesMenu = ['Cadastrar Produto', 'Consultar Estoque', 'Resgistrar Entrada', 'Registrar Saida']
    for index, opcao in enumerate(opcaoesMenu, start=1):
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



        produto = {
                    "codigo": codigo,
                    "nome": nome,
                    "quantidadeinical": quantidadeinical,
                    "estoqueMinimo": estoqueMinimo,
                }
        estoque.append(produto)

        op = input("deseja cadastrar mais produtos ? [S/N]")
        if op in "Ss":
            continue
        print("produtos cadastrados: ")
        print(estoque)
        break


def main():
    while True:
        menuDoSistema()
        op = input("Escolha uma opção valida: ")
        if op == "1":
            cadastrarProduto(estoque)
            os.system("cls")


if __name__ == "__main__":
    main()
