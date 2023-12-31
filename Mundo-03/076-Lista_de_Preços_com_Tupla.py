"""
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

produtos = ("lapiz", 1.75, "borracha", 2.00, "caderno",15.90,"estojo",25.00,"transferidor", 4.20, "compasso", 9.99, "mochila", 120.00, "caneta", 22.30, "livros", 34.90)

for pos,nome in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{nome:.<30}',end='')
    else:
        print(f"R${nome: >5}",end='')
        print()