"""
Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import cos,sin,tan,radians
ang = float(input('Digite o Angulo: '))
angr = radians(ang)
seno = sin(angr)
cosseno = cos(angr)
tangente = tan(angr)
print(f'O Ângulo {ang}° tem:\nseno = {seno:.2f};\ncosseno = {cosseno:.2f}\ntangente = {tangente:.2f}')
