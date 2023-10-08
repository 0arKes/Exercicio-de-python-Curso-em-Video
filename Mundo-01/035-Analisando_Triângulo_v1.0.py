"""
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

r1 = float(input('r1: '))
r2 = float(input('r2: '))
r3 = float(input('r3: '))

if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print(f'Os Segmentos {r1}, {r2} e {r3}, Podem formar um triângulo')
else:
    print(f'Os Segmentos {r1}, {r2} e {r3}, NÃO Podem formar um triângulo')
