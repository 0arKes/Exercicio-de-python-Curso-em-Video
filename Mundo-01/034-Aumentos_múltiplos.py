"""
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

sal = int(input('Digite o seu Salário: '))
if sal > 1250:
    print(f'Seu salário ficará R${sal * 1.1:.2f}')
else:
    print(f'Seu salário ficará R${sal * 1.15:.2f}')
