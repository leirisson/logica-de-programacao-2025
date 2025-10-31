# 2. Calculadora Simples
# Elabore um programa que leia dois números e exiba um menu com as
# operações: soma, subtração, multiplicação, divisão e resto inteiro. Use
# switch-case para realizar a operação escolhida e mostrar o resultado final.

import os

while True:
    os.system("cls")
    print("🟰"*50)
    print("CALCULADORA SIMPLES")
    print("🟰"*50)
    print("1 - Somar ➕")
    print("2 - Subtrair ➖")
    print("3 - Multiplicar ✖️")
    print("4 - Dividir ➗")
    print("5 - Sair 📤")
    print("="*50)
    op = int(input("Escolha uma opção: "))
    print(op)
    
    match op:
        case 1:
            os.system("cls")
            print("➕"*30)
            print("SOMA SIMPLES ")
            print("➕"*30)
            numero1 = int(input("Digite o primeiro valor: "))
            numero2 = int(input("Digite o segundo valor: "))
            soma = numero1 + numero2
            print(f"Soma dos valores é: {soma}")
            input("presione qualquer tecla par continuar...")
        case 2:
            os.system("cls")
            print("➖"*30)
            print("SUBTRAÇÃO SIMPLES")
            print("➖"*30)
            numero1 = int(input("Digite o primeiro valor: "))
            numero2 = int(input("Digite o segundo valor: "))
            subtracao = numero1 - numero2
            print(f"Soma dos valores é: {subtracao}")
            input("presione qualquer tecla par continuar...")
        case 3:
            os.system('cls')
            print("✖️"*30)
            print("MULTIPLICAÇÃO SIMPLES")
            print("✖️"*30)
            numero1 = int(input("Digite o primeiro valor: "))
            numero2 = int(input("Digite o segundo valor: "))
            multiplicacao = numero1 * numero2 
            print(f"O o resultador da multiplicação é: {multiplicacao}")
            input("aperte em qualquer tecla para continuar")
        case 4:
            os.system('cls')
            print("➗"*30)
            print("DIVISÃO SIMPLES")
            print("➗"*30)
            numero1 = int(input("Digite o primeiro valor: "))
            numero2 = int(input("Digite o segundo valor: "))
            divisao = numero1 / numero2
            print(f"o resultado da divisão é: {divisao:.2f}")
            input("Aperte em qualquer tecla para continuar....")
        case 5:
            os.system('cls')
            print("📤"*30)
            print("SAINDO DO SISTEMA...")
            print("📤"*30)
            break
        case _:
            os.system('cls')
            print("☢️"*30)
            print("OPÇÃO INVALIDA")
            print("TENTE NOVAMENTE")
            print("☢️"*30)
            input("Aperte qualquer tecla para continuar...")
            