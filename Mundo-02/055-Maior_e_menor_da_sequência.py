"""
Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""

pesoMaior = 0.0
pesoMenor = 0.0

for c in range(1,6):
    pesoGeral = float(input(f"Digite o peso da {c}º pessoa: "))
    if c == 1:
        pesoMaior = pesoGeral
        pesoMenor = pesoGeral

    else:
        if pesoGeral > pesoMaior:
            pesoMaior = pesoGeral
        elif pesoGeral < pesoMenor:
            pesoMenor = pesoGeral

print (f"O MAIOR peso foi: {pesoMaior}Kg e o MENOR foi: {pesoMenor}Kg")