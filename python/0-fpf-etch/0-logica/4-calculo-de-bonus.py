# 4 -> Cálculo de Bônus
# Crie um programa que solicite o salário de um funcionário e calcule o valor
# do bônus de acordo com a faixa salarial. Se o salário for inferior a 1000, o
# bônus deve ser de 20%; caso contrário, de 10%. Exiba o valor final com o
# bônus incluído.

while True:
    salario = float(input("inform o salario do colaborador: "))
    if(salario < 1000):
        bonus = salario * 0.2
        novoSalario = salario + bonus
        print("Seu novo salario é: ", novoSalario)
        op = input("Deseja calcular outro salario ?, [S - Sim / N - Não]:  ")
        if(op in "Ss"):
            break
        else:
            break
        
    else:
        bonus = salario * 0.1
        novoSalario = salario + bonus
        print("Seu novo salario é: ", novoSalario)
        op = input("Deseja calcular outro salario ?, [S - Sim / N - Não]:  ")
        if(op in "Ss"):
            break
        else:
            break
        