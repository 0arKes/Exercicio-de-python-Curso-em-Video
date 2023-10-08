"""
Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

x = int(input('Digite um numero de 0 a 9999: '))

u = x % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10

print(f'Unidade = {u}')
print(f'Dezena = {d}')
print(f'Centena = {c}')
print(f'Milhar {m}')