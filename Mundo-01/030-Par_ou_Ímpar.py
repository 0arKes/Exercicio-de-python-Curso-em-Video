"""
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

x = int(input('Digite um número: '))
if x % 2 == 0:
    print(f'\033[1;36m{x} é par')
else:
    print(f'\033[1;31m{x} é impar')
