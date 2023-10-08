"""
Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

nome = input('Digite seu nome: ')
print(f'M = {nome.upper()}')
print(f'mn = {nome.lower()}')
spc = nome.count(' ')
print(f'Seu nome tem: {len(nome)-spc} Carctéres')
print(f'Primeiro nome = {nome.split()[0]} e tem {len(nome.split()[0])} Caractéres')
