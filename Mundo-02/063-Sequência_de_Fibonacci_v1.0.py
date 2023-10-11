"""
Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8"""

c = 0
t1 = 1
t2 = 0

n = int(input("Digite o valor de 'n' (para mostrar os termos da sequência de Fribonati 'n' vezes): "))

while n > 0:
    c = t1 + t2
    t1 = t2
    t2 = c
    print(f"[{c}]", end='')
    print("->" if n-1 != 0 else '', end='')
    n -= 1
