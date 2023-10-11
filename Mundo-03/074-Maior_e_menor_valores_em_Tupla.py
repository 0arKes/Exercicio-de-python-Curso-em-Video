"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

import random

x1 = random.randint(0,10)
x2 = random.randint(0,10)
x3 = random.randint(0,10)
x4 = random.randint(0,10)
x5 = random.randint(0,10)

t = (x1,x2,x3,x4,x5)
menor = 0
maior = 0

for c in range(0,len(t)):
    if c == 0:
        menor = t[c]
        maior = t[c]
    else:
        if t[c] < menor:
            menor = t[c]
        if t[c] > maior:
            maior = t[c]

print(f"Sua lista foi: {t} e o menor valor da lista é: {menor} e o maior é: {maior}")

#Solução 2
'''
import random

n = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))

print(20*"-=")
print(f"A lista gerado foi:\n{n}")
print(20*"-=")
print(f"o maior valor da lista é {max(n)} & o menor valor foi {min(n)}")
'''