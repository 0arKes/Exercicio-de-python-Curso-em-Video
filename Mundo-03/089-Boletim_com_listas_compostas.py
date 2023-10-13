"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

alunos = []
media = 0

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("N1: "))
    nota2 = float(input("N2: "))
    media = (nota1+nota2) /2
    alunos.append([nome, [nota1,nota2],media])

    c = str(input("Continuar S/n: ")).strip().lower()[0]
    if c == "n":
        break

print()
print(50*'-=')
print()
print(f'{"NOME:":<10}{"NOTAS:":<15}{"MÉDIA:":>10}')
print(40*'-')

for a in alunos:
    print(f'{a[0]:<10}', end='')
    print(f'{a[1]}',end='')
    print(f'{a[2]:>13}')

