"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

import random
import time

jogos = []
aux = []
cont = 0
num = 0
quantjogos = int(input("Quantos jogos serão feitos: "))

while quantjogos > 0:
    while True:
        num = random.randint(1,60)
        
        if num not in aux:
            aux.append(num)

        if len(aux) == 6:
            break


    quantjogos -= 1
    jogos.append(aux[:])
    aux.clear()

for j in jogos:
    time.sleep(1)
    cont +=1
    print(f"O {cont}º Jogo é {j}")