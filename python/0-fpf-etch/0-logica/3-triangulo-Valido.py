# 3 - Triângulo Válido
# Desenvolva um programa que leia três valores correspondentes aos lados
# de um triângulo e verifique se eles podem formar um triângulo válido. Caso
# positivo, classifique-o como equilátero, isósceles ou escaleno, exibindo a
# categoria correta.


ladoA = float(input("digite o primeiro lado do triangulo: "))
ladoB = float(input("digite o segundo lado do triangulo: "))
ladoC = float(input("digite o terceiro lado do triangulo: "))

if(ladoC < ladoA + ladoB and ladoB < ladoA + ladoC and ladoA < ladoB + ladoC):
    print("Este triangulo é valido...")
    if(ladoA == ladoB and ladoA == ladoC and ladoB == ladoC):
        print("este é um Triângulo Equilátero")
    elif(ladoA == ladoB or ladoA == ladoC):
        print("este é um Triângulo Isósceles")
    else:
        print("Triângulo Escaleno, Possui os três lados com medidas diferentes entre si.")
    
else:
    print("esse triangulo não é valido...")
    