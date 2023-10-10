"""
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
"""

n1 = float(input("Digite a PRIMEIRA nota: "))
n2 = float(input("Digite a SEGUNDA nota:"))
n3 = float(input("Digite a TERCEIRA nota: "))

if (n1 + n2 + n3)/3 <= 5:
    print("\033[31mVocê Reprovou")
elif (n1+n2+n3)/3 >5 and (n1+n2+n3)/3 < 6.9:
    print ("\033[33mVocê está em RECUPERAÇÃO")
else:
    print("\033[36mVocê PASSOU")
