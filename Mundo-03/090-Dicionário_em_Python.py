"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

aluno = {}

aluno["Nome"] = str(input("Digite o nome: "))
aluno["Média"] = float(input(f"Digite a média de: {aluno['Nome']}: "))

if aluno["Média"] < 7:
    aluno["Situação"] = "Reprovado"
else:
    aluno["Situação"] = "Aprovado"

print()

for k,v in aluno.items():
    print(f"{k} = {v}")

print()