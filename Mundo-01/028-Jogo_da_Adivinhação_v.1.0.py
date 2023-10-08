"""
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random

var = random.randint(1,5)
print('Pensando em um número...')
n = int(input('Chute o número que eu pensei: '))

if n == var:
    print('You Win')
else:
    print('You Lose')
print('End Game')
