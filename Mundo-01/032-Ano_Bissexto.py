"""
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

ano = int(input('Informe o Ano: '))
bissexto = ano % 4
if bissexto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano {ano} é Bissexto')
else:
    print(f'O Ano {ano} Nõo é Bissexto')
