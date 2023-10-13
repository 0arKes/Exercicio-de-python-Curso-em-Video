"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def area(l, c):

    a = l*c
    print(f"A área de um terreno {l}x{c} = {a}m²")


area(float(input("Largura (m): ")), float(input("Comprimento (m): ")))