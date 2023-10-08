"""
Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

prod = float(input('Digite o valor do produto: '))
porcent = (prod*5)/100
print(f'Preço: R${prod}\n5% de desconto: R${prod-porcent}')
