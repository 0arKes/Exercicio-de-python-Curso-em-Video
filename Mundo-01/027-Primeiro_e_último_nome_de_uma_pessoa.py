"""
Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = input('Digite seu nome completo: ')
nome = nome.title().split()
print(f'Nome: {nome[0]}')
print(f'Sobrenome: {nome[-1]}')
