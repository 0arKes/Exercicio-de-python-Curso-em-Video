"""
Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

dia = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos km foram rodados? '))
print(f'Valor Final à pagar {(dia*60)+(km*0.15)}')
