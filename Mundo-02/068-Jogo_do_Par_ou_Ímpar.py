"""
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
"""

import random

numComputador = random.randrange(1,10)
escolha = str(input("P ou I: "))
numJogador = int(input("Digite um número entre 1 e 10: "))
soma = numJogador + numComputador
vitoria = 0

while True:
    print (f"\033[35mO Computador jogou {numComputador}")

    if escolha in "Pp" and soma % 2 == 0:
        print("\033[34mVocê VENCEU")

    elif escolha in "Pp" and soma % 2 != 0:
        print ("\033[31mVocê PERDEU")
        break

    elif escolha in "Ii" and soma % 2 != 0:
        print("\033[34mVocê VENCEU")

    elif escolha in "Ii" and soma % 2 == 0:
        print("\033[31mVocê PERDEU")
        break

    numComputador = random.randrange(1,10)
    escolha = str(input("P ou I: "))
    numJogador = int(input("Digite um número entre 1 e 10: "))
    soma = numJogador+numComputador
    vitoria += 1

print(f"\033[36mVocê ganhou {vitoria} vezes")
