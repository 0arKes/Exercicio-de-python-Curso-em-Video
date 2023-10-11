"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

n = int(input("Digite um número: "))
f = 1
for n in range(n, 0, -1):
    f *= n
    print(n, end='')
    print(" x " if n > 1 else " = ", end='')

print(f)