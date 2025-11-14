import os, time

# lista de dicionarios:
livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "isbn": "978-85-273-0077-1",
        "preco": 45.90,
        "estoque": 32
    },
    {
        "id": 2,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "isbn": "978-85-9508-320-5",
        "preco": 89.90,
        "estoque": 15
    },
    {
        "id": 3,
        "titulo": "1984",
        "autor": "George Orwell",
        "isbn": "978-85-359-1485-5",
        "preco": 52.00,
        "estoque": 27
    },
    {
        "id": 4,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "isbn": "978-85-9508-123-2",
        "preco": 29.90,
        "estoque": 50
    },
    {
        "id": 5,
        "titulo": "O Alquimista",
        "autor": "Paulo Coelho",
        "isbn": "978-85-7684-840-2",
        "preco": 39.90,
        "estoque": 41
    }
]

# lista de livros vendidos 
vendas = []
# função para iniciar o carregamento da barra do sistema
def carregar_sistema():
    tamanho_barra = len("INCIANDO O SISTEMA")
    for i in range(tamanho_barra):
        os.system("cls")
        print("INCIANDO O SISTEMA")
        print('='*i)
        time.sleep(.1)

def pausar_sistema(tempo):
    time.sleep(tempo)

# função para limpar o terminal da aplicação
def limpar_tela():
    os.system("cls")

#função responsael po exibir o menu do sistema
def titulo_sistema(titulo):
    print("=" * len(titulo))
    print(titulo)
    print("=" * len(titulo))

def menu_sistema(opcoes_menu):
    for i, indice in enumerate(opcoes_menu):
        print(indice)

# função responsavel por cadastrar o livro
def cadastrar_livro():
    proximo_id = len(livros) + 1
                # título, autor, ISBN, preço, quantidade_estoque
    while True:
        titulo = input("informe o titulo do livro: ")
        if len(titulo) == 0:
            print("O titulo é obrigatorio. Informe um titulo para o livro:")
            continue
        else:
            break
                    
    while True:
        autor = input("qual o nome do autor: ")
        if len(autor) == 0:
            print("O autor é obrigatorio. Informe um nome para o autor:")
            continue
        else:
            break
                                
    while True:
        isbn = input("qual o ISBN do livro: ").strip()
        isbn_ja_existe = False
        for lv in livros:
            if lv["isbn"] == isbn or len(isbn) == 0 or len(isbn) <=10:
                isbn_ja_existe = True
                break
            
        if isbn_ja_existe:
            print("ISBN já cadastrado ou em branco. Por favor, informe um ISBN válido (não repetido).")
            print("ISBN deve ter pelo menos 10 caracteres")
            print("ISBN deve ficar em branco")
        else:
            break
                    
    while True:
            preco = float(input("qual o preço do livro: "))
            estoque = int(input("quantidade: "))
            if preco >= 0 and estoque >= 0:
                break
            else:
                print("Preço e Estoque devem ser maior que zero")
                    
            
    livro = {
            "id":proximo_id,
            "titulo": titulo,
            "autor":autor,
            "preco":preco,
            "isbn": isbn,
            "estoque":estoque
        }
        
    
    livros.append(livro)
    print("livro cadastrado com sucesso !")

#função responsavel pelo estoque
def consultar_estoque():
# 1. Solicitar termo de busca (título ou ISBN)
    chave_pesquisa = input("informe o ISBN ou TITULO do livro: ").lower()
    
    livro_encontrado = False
    
    for livro in livros:
        if(livro['isbn'] == chave_pesquisa or  livro['titulo'].lower() == chave_pesquisa ):
            print(f"ID: {livro['id']}")
            print(f"TÍTULO: {livro['titulo']}")
            print(f"AUTOR: {livro['autor']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"PREÇO: {livro['preco']}")
            print(f"ESTOQUE: {livro['estoque']}")
            livro_encontrado = True
        elif len(chave_pesquisa) == 0:
            print(f"ID: {livro['id']}")
            print(f"TÍTULO: {livro['titulo']}")
            print(f"AUTOR: {livro['autor']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"PREÇO: {livro['preco']}")
            print(f"ESTOQUE: {livro['estoque']}")
            print("="*20)
            livro_encontrado = True
    if not livro_encontrado:
        print("Livro não encontrado.")
            
# função responsavel por reposição no estoque
def reposicao_estoque():
    pass

#função responsavel pela venda
def vendas_livro():
    chave_buscar = input("informe o título ou o isbn do livro: ")
    livroEncontrado = False
    
    for livro in livros:
        if livro['isbn'] == chave_buscar or livro['titulo'].lower() == chave_buscar.lower():
            quantidade = int(input("quantidade: "))
            if(livro['estoque'] >= quantidade):
                print("quantidade disponivel")
            livroEncontrado = True
    
    if not livroEncontrado:
        print("livro não encontrado")
# função responsavel pelos relatorios do sistema
def relatorios_sistema():
    pass

# declarar as funções dentro do main 
def main():
    carregar_sistema()
    limpar_tela()
    
    
    while True:
        titulo_sistema("SISTEMA: Controle de Estoque de Livros")
        menu_sistema([
            '1 - Cadastro de Livros 📚', 
            '2 - Consultar Estoque 📦',
            '3 - Realizar Venda 🪙💵',
            '4 - Reposição de Estoque em dev 📦🔁',
            '5 - Relatório de Estoque Baixo  em dev 📜🧮',
            '0 - Sair ⬇ 🚹🚺'
            ])
        op = input("escolha sua opção: ")
        
        match(op):
            case "1":
                cadastrar_livro()
                limpar_tela()
            case "2":
                consultar_estoque()
                input("digite qualquer tecla para continuar.")
                pausar_sistema(1)
                limpar_tela()
            case "3":
                vendas_livro()
                input("digite qualquer tecla para continuar.")
                pausar_sistema(1)
                limpar_tela()
            case "0":
                break
            case _:
                print("opção invalida.")
                print("Escolha um opção valida.")
                continue
    
# responsavel por incializar o sistema
if __name__ == "__main__":
    main()