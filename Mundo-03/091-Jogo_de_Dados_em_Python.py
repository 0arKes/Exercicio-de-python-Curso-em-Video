"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

import random
from time import sleep

jogadores = {}
cont = 1

jogadores["j1"] = random.randint(1,6)
jogadores["j2"] = random.randint(1,6)
jogadores["j3"] = random.randint(1,6)
jogadores["j4"] = random.randint(1,6)


for j, d in jogadores.items():
    sleep(1)
    print(f"O {j} tirou {d}")

print(40*'=-')
print(f'{"Ranking":>42}')
print(40*'=-')

for c in range(6,0,-1):
    for j, d in jogadores.items():    
        if c == d:
            print(f'{cont}º = {j}')
            cont += 1