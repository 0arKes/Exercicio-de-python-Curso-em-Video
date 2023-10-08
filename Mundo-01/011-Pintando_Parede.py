"""
Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

lar = float(input('Digite a largura em métros: '))
alt = float(input('Digite a altura em métros: '))
area = lar*alt
print(f'Será necessário {area/2}l de tinta para pintar {area}m² de parede')
