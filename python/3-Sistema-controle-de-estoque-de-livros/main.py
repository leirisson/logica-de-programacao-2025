import os, time

# array de dicionarios:
livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "isbn": "978-85-273-0077-1",
        "preco": 45.90,
        "quantidade_estoque": 32
    },
    {
        "id": 2,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "isbn": "978-85-9508-320-5",
        "preco": 89.90,
        "quantidade_estoque": 15
    },
    {
        "id": 3,
        "titulo": "1984",
        "autor": "George Orwell",
        "isbn": "978-85-359-1485-5",
        "preco": 52.00,
        "quantidade_estoque": 27
    },
    {
        "id": 4,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "isbn": "978-85-9508-123-2",
        "preco": 29.90,
        "quantidade_estoque": 50
    },
    {
        "id": 5,
        "titulo": "O Alquimista",
        "autor": "Paulo Coelho",
        "isbn": "978-85-7684-840-2",
        "preco": 39.90,
        "quantidade_estoque": 41
    }
]

# função para iniciar o carregamento da barra do sistema
def carregar_sistema():
    tamanho_barra = len("INCIANDO O SISTEMA")
    for i in range(tamanho_barra):
        os.system("cls")
        print("INCIANDO O SISTEMA")
        print('='*i)
        time.sleep(.1)

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

# declarar as funções dentro do main 
def main():
    carregar_sistema()
    limpar_tela()
    titulo_sistema("SISTEMA: Controle de Estoque de Livros")
    menu_sistema(['1 - Cadastro de Livros'])
    
# responsavel por incializar o sistema
if __name__ == "__main__":
    main()