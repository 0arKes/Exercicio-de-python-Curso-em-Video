"""
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

p = int(input("Digite o PRIMEIRO termo: "))
r = int(input("Digite a razão: "))
ultimo = p + (10*r)

while p < ultimo:
    print(f"[{p}]",end='')
    print("->" if p != ultimo-r else "", end='')
    p = p + r
