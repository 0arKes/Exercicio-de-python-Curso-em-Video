"""
Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

metros = float(input('Digite um valor em metros(m): '))

print(f'{metros/1000}Km')
print(f'{metros/100}Hm')
print(f'{metros/10}Dam')
print(f'{metros}M')
print(f'{metros*10}Dm')
print(f'{metros*100}Cm')
print(f'{metros*1000}Mm')
