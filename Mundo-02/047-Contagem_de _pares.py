"""
Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

for c in range(0,51):
    if c % 2 == 0:
        print(f"\033[34mO Número {c} é PAR")
    else:
        print(f"\033[31mO Número {c} é ÍMPAR")