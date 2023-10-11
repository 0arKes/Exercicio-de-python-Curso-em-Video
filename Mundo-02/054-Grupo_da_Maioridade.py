"""
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

menores = int()
maiores = int()
ano = date.today().year

for c in range(1,8):
    nasc = int(input(f"Digite o ano de nascimento da {c}º pessoa: "))
    if ano - nasc >= 18:
        maiores +=1
    else:
        menores+=1
print(f"{maiores} Pessoas são maiores")
print(f"{menores} Pessoas são menores")
