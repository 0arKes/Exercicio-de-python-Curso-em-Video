"""
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
"""

import random
import time

escolha = int(input("[1] para TESOURA\n[2] para PEDRA\n[3] para PAPEL "))
computador = random.randrange(1,4)

print(20*'-=')
time.sleep(0.5)
print('Jo')
time.sleep(0.5)
print('Ken')
time.sleep(0.3)
print('Pô')
time.sleep(0.5)

if escolha == computador:
    if escolha == 1:
        print('Você e o Computador Jogaram TESOURA')
    elif escolha == 2:
        print('Você e o Computador Jogaram PEDRA')
    else:
        print('Você e o Computador Jogaram PAPEL')
    print("\033[33m Deu Empate")

elif escolha == 1:
    if computador == 2:
        print('Você jogou TESOURA e o Computador Jogou Pedra')
        print("\033[31m Você Perdeu")
    elif computador == 3:
        print('Você jogou TESOURA e o Computador Jogou PAPEL')
        print("\033[34m Você Venceu")

elif escolha == 2:
    if computador == 1:
        print('Você jogou PEDRA e o Computador Jogou TESOURA')
        print("\033[34m Você Venceu")
    elif computador == 3:
        print('Você jogou PEDRA e o Computador Jogou PAPEL')
        print("\033[31m Você Perdeu")
elif escolha == 3: 
    if computador == 1:
        print('Você jogou PAPEL e o Computador Jogou TESOURA')
        print("\033[31m Você Perdeu")
    elif computador == 2:
        print('Você jogou PAPEL e o Computador Jogou PEDRA')
        print("\033[34m Você Venceu")

