from random import choice

x1 = input('Primeiro aluno: ')
x2 = input('Segundo aluno: ')
x3 = input('Terceiro aluno: ')
x4 = input('Quarto aluno: ')
x = x1,x2,x3,x4
print(f'O aluno ESCOLIDO foi: {choice(x)}')
