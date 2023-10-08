"""
Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

temp = float(input('Digite o valor da temperatura em C°: '))
f = (temp*1.8)+32
print(f'{temp}C°, ou {f}F°')
