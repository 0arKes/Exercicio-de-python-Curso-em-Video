"""
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

x1 = int(input('Digite o PRIMEIRO valor: '))
x2 = int(input('Digite o SEGUNDO valor: '))
x3 = int(input('Digite o TERCEIRO valor: '))

if x1 > x2 and x1 > x3:
    print(f'O MAIOR número é {x1}')
    if x2 < x3:
        print(f'E o MENOR é {x2}')
    else:
        print(f'E o MENOR é {x3}')

elif x2 > x1 and x2 > x3:
    print(f'O MAIOR número é {x2}')
    if x1 < x3:
        print(f'E o MENOR é {x1}')
    else:
        print(f'E o MENOR é {x3}')

else:
    print(f'O MAIOR número é {x3}')
    if x1 < x2:
        print(f'E o MENOR é {x1}')
    else:
        print(f'E o MENOR é {x2}')
print()
