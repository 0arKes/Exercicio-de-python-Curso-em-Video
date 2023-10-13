"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""

from time import sleep

def contar(i,f,p):
    
    if p == 0:
        p = 1
    if i > f:
        p *= -1

    for c in range(0,11):
        print(c, end=' ')
    print()

    for c in range(10,0,-2):
        print(c, end=' ')
    print()

    for c in range(i,f,p):
        print(c, end=' ')


contar(int(input("Inicio: ")),int(input("Fim: ")),int(input("Passo: ")))