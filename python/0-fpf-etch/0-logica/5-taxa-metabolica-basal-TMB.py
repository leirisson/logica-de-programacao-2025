# 5 - Taxa Metabólica Basal (TMB)
# Desenvolva um programa que calcule a Taxa Metabólica Basal (TMB) de
# uma pessoa com base no sexo, peso, altura e idade.
# ● Homem: 88,362 + (13,397 × peso) + (4,799 × altura) − (5,677 × idade)
# ● Mulher: 447,593 + (9,247 × peso) + (3,098 × altura) − (4,330 × idade)
# Exiba o valor da TMB calculada com duas casas decimais.

import os

while True:
    os.system("cls")
    print("🟩"*len("taxa metabolica basal"))
    print("TAXA METABOLICA BASAL")
    print("🟩"*len("taxa metabolica basal"))
    print("1 - HOMEM 👨")
    print("2 - MULHER 👩")
    print("0 - SAIR 📤")
    print("🟩"*len("taxa metabolica basal"))
    op = int(input("ESCOLHA UMA OPÇÃ: "))
    
    match (op):
        case 1:
            os.system("cls")
            print("🟥"* len("informe os dados do usuario"))
            print("INFORME OS DADOS DO USUARIO")
            print("🟥" * len("informe os dados do usuario"))
            
            peso = float(input("Qual o peso do usuario: "))
            idade = int(input("Qual a idade do usuario: "))
            altura = float(input("Qual a altura do usuario: "))
            
            tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
            
            os.system("cls")
            print("🟥"* len("RESULTADO DA CONSULTA"))
            print("RESULTADO DA CONSULTA")
            print("🟥"* len("RESULTADO DA CONSULTA"))
            print(f"🎉⚡ - Taxa metabolica: {tmb:.2f}")
            input("aperte qualquer tecla para continuar ...")
            os.system("cls")
            
        
        case 2:
            os.system("cls")
            print("🟥"* len("informe os dados do usuario"))
            print("INFORME OS DADOS DO USUARIO")
            print("🟥" * len("informe os dados do usuario"))
            
            peso = float(input("Qual o peso do usuario: "))
            idade = int(input("Qual a idade do usuario: "))
            altura = float(input("Qual a altura do usuario: "))
            
            tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
            
            os.system("cls")
            print("🟥"* len("RESULTADO DA CONSULTA"))
            print("RESULTADO DA CONSULTA")
            print("🟥"* len("RESULTADO DA CONSULTA"))
            print(f"🎉⚡ - Taxa metabolica: {tmb:.2f}")
            input("aperte qualquer tecla para continuar ...")
            os.system("cls")
        
        case 0:
            os.system("cls")
            print("🟥"* len("informe os dados do usuario"))
            print("SISTEMA FINALIZADO ...")
            print("🟥" * len("informe os dados do usuario"))
            break
    
        case _:
            os.system("cls")
            print("🟥"* len("informe os dados do usuario"))
            print("OPÇÃO SELECIONADA INVALIDA...")
            print("TENTE OUTRA OPÇÃO.")
            print("🟥" * len("informe os dados do usuario"))
            input("apertem em qualquer tecla para continuar...")
            
        
    
    
    