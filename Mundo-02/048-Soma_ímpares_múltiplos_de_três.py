"""
Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
soma = 0

for c in range (1,501,2):
    if c%3 == 0:
        soma += c
        print(c,end='')
        print('+' if c != 495 else '=',end='')
print(f'\033[34m{soma}')