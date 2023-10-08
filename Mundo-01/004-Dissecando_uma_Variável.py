"""
Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""

txt = input('Digite algo: ')

print(type(txt))
print(f'Apenas espaços? {txt.isspace()}')
print(f'É um numero? {txt.isnumeric()}')
print(f'É alfabético? {txt.isalpha()}')
print(f'É alfanumérico? {txt.isalnum()}')
print(f'Esta em minúsculas? {txt.islower()}')
print(f'Esta em maiúsculas? {txt.isupper()}')
print(f'Esta captalizada? {txt.istitle()}')