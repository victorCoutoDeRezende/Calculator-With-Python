"""
código que cria uma calculadora com as principais operações matemáticas
a calculadora possui as 4 operações aritméticas: Adição(+), Subtração(-), Multiplicação(x) e Divisão(/)
além disso, ela possui outras 3 operações: Fatorial(!), Raiz Quadrada(√) e Exponenciação(^)
o código verifica, em cada campo de entrada de dados, se o usuário digitou o tipo correto de dado no campo
o código também mostra uma mensagem de abertura, que deixa o programa mais amigável para o usuário
por fim, a calculadora pergunta se o usuário quer fazer mais operações matemáticas. Caso a resposta seja sim, a calculadora reinicia seu estado
permitindo que novas operações sejam realizadas"""
import math
import sys
import os
from time import sleep
os.system("cls")
def mensagem_abertura(msg):
    tam = len(msg)
    print("-="*tam)
    print(msg.center(50))
    print("-=" * tam)
    print("\n")
    print("[1]Calculos Aritméticos", " [2]Fatorial", " [3]Raiz Quadrada", " [4]Exponenciação")
def aritmeticos(escolha):
    print("[1]Adição", "[2]Subtração", "[3]Multiplicação", "[4]Divisão")
    while True:
        try:
            escolha = int(input("-> "))
            break
        except ValueError:
            print("\nOops! Não é uma opção válida.  Tente novamente")
            aritmeticos(escolha)
    match escolha:
        case 1:                                         #Adição
            adiciona1 = input("Digite um número: ")
            adiciona2 = input("Digite outro número: ")
            if adiciona1.isnumeric() and adiciona2.isnumeric():
                adiciona1, adiciona2 = float(adiciona1), float(adiciona2)
                resultado(adiciona1 + adiciona2)
            else:
                print("Você precisa digitar um número nas duas parcelas")
                executa_outra()
        case 2:                                         #Subtração
            minuendo = input("Digite o minuendo: ")
            subtraendo = input("Digite o subtraendo: ")
            if minuendo.isnumeric() and subtraendo.isnumeric():
                minuendo, subtraendo = float(minuendo), float(subtraendo)
                resultado(minuendo - subtraendo)
            else:
                print("Você precisa digitar um número tanto no minuendo, quanto no subtraendo")
                executa_outra()
        case 3:                                         #Multiplicação
            multiplicando = input("Digite o multiplicando: ")
            multiplicador = input("Digite o multiplicador: ")
            if multiplicando.isnumeric() and multiplicador.isnumeric():
                multiplicando, multiplicador = float(multiplicando), float(multiplicador)
                resultado(multiplicando * multiplicador)
            else:
                print("Você precisa digitar um número tanto no multiplicando, quanto no multiplicador")
                executa_outra()
        case 4:                                         #Divisão
            dividendo = input("Digite o dividendo: ")
            divisor = input("Digite o divisor: ")
            try:
                if dividendo.isnumeric() and divisor.isnumeric():
                    dividendo, divisor = float(dividendo), float(divisor)
                    resultado(dividendo / divisor)
                else:
                    print("Você precisa digitar um número tanto no multiplicando, quanto no multiplicador")
                    executa_outra()
            except ZeroDivisionError:
                print("Divisão por 0 não está definida")
                pergunta_outra()
        case _:
            print("\nOops! Não é uma opção válida.  Tente novamente")
            aritmeticos(escolha)
def pergunta_outra():
    print("Que fazer outra operação? [s]sim, [n]não")
    teste = input("->")
    if teste == "s":
        executa_outra()
    elif teste == "n":
        sys.exit()
    else:
        print("Opção inválida, digite [s]para sim e [n]para não\n")
        sleep(2)
        os.system("cls")
        pergunta_outra()
def executa_outra():    #Reinicia a calculadora
    sleep(2)
    os.system("cls")
    calculadora()
def resultado(result):
    print("O Resultado é: ", result)
    pergunta_outra()
def calculadora():
    mensagem_abertura("Qual cálculo deseja fazer?")
    while True:  #Este loop força o usuário a digitar um número
        while True:
            try:
                escolha = int(input("-> "))
                break
            except ValueError:
                print("\nOops! Não é uma opção válida.  Tente novamente")
                executa_outra()
        if escolha == 1:                                #Operações Aritméticas
            aritmeticos(escolha)
        elif escolha == 2:                              #Fatorial de um Número
            fatorial = input("Digite o número: ")
            if fatorial.isnumeric():
                fatorial = int(fatorial)
                resultado(math.factorial(fatorial))
            else:
                print("Você precisa digitar um número")
                executa_outra()
        elif escolha == 3:                              #Raiz Quadrada
            raiz = input("Digite um número: ")
            if raiz.isnumeric():
                raiz = float(raiz)
                resultado(math.sqrt(raiz))
            else:
                print("Você precisa digitar um número")
                executa_outra()
        elif escolha == 4:                              #Exponenciação
            base = input("Digite a base: ")
            expoente = input("Digite o expoente: ")
            if base.isnumeric() and expoente.isnumeric():
                base, expoente = int(base), int(expoente)
                resultado(math.pow(base, expoente))
            else:
                print("Você precisa digitar um número tanto na base, quanto no expoente")
                executa_outra()
        else:
            print("\nOops! Não é uma opção válida.  Tente novamente")
            executa_outra()
calculadora()
