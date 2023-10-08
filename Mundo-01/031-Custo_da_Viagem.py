"""
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""

dis = int(input('Digite a distância (km): '))
if dis <= 200:
    print(f'Você irá Pagar: R${dis*0.5:.2f}')
else:
    print(f'Você irá Pagar: R${dis*0.45:.2f}')
