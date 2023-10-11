"""
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

import random

Ncomputador = random.randrange(1,10)
Perdas = 0
venceu = False

while not venceu:
    Njogador = int(input("Chute um número entre 1 e 10: "))
    Perdas += 1

    if Njogador == Ncomputador:
        venceu = True
    else:
        if Njogador > Ncomputador:
            print("Tente algo MENOR...")
        else:
            print("Tente algo MAIOR...")

print(f"Você acertou, o número era {Ncomputador} e você teve {Perdas} tentativas")