"""
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

vel = int(input('Digite a velocidade do seu carro: '))
if vel > 80:
    print('Você foi multado')
    valor = vel - 80
    print(f'O valor da sua multa é de {valor*7}')
    