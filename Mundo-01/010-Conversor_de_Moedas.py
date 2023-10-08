"""
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

din = float(input('Quanto dinheiro você tem: '))
print(f'Com {din}, você pode comprar {(din/5.17):.2f} Dólares')
