"""
Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
"""

cid = input('Digite o nome da  sua cidade: ')
cid = cid.title().split()
print('Santo' in cid[0])
