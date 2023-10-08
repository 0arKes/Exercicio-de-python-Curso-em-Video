"""
Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle
a1 = input('Primeiro: ')
a2 = input('Segundo: ')
a3 = input('Terceiro: ')
a4 = input('Quarto: ')
lista = [a1,a2,a3,a4]
shuffle(lista)
print('A ordem será: ')
print(lista)
