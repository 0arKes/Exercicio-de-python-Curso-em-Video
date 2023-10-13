"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

import random

lista =[]


def sorteia(l):
    for c in range(0,5):
        l.append(random.randint(1,5))
        print(f"O {c+1}º valor é {l[c]}")
    print()


print()


def somapar(l):
    soma = 0
    for x in range(0,5):
        if l[x] % 2 == 0:
            print(f"{l[x]} é PAR")
            soma += l[x]
    print(f'A soma total é {soma}')
    print()



sorteia(lista)
somapar(lista)