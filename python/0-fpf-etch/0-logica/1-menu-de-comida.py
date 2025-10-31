# 1. Menu de Comidas
# Crie um programa que apresente um menu com diferentes opções de
# comida (
    # 1-  como pizza, 
    # 2 - hambúrguer, 
    # 3 - salada  
    # 4 - sushi
    # ). O usuário deve escolher
# uma opção, e o programa deve exibir uma mensagem correspondente à
# escolha, utilizando a estrutura switch-case.

import os

while True:
    print("=========================")
    print("Escolha uma opção a menu ")
    print("=========================")
    print("1 - Pizza")
    print("2 - hambúrguer")
    print("3 - salada")
    print("4 - sushi")
    print("5 - sair", end=" ")
    op  = input("")
    
    if op == "5":
        break
    elif op == "1":
        os.system("cls")
        print("=========================")
        print("Opção Escolhida no menu  ")
        print("=========================")
        print("Você escolheu pizza.")
        break
    elif op == "2":
        os.system("cls")
        print("=========================")
        print("Opção Escolhida no menu  ")
        print("=========================")
        print("você escolheu hambúrgue.")
        break
    elif op == "3":
        os.system("cls")
        print("=========================")
        print("Opção Escolhida no menu  ")
        print("=========================")
        print("você escolheu salada.")
        break
    elif op == "4":
        os.system("cls")
        print("=========================")
        print("Opção Escolhida no menu  ")
        print("=========================")
        print("você escolheu sushi.")
        break
    else:
        os.system("cls")
        print("=========================")
        print("Opção Escolhida no menu  ")
        print("=========================")
        print("Escolheu a opção invalida")
        input("tente novamente, ... aperte qualquer tecla.")
        os.system("cls")