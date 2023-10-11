"""
Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

idademedia = 0
idadevelho = 0
nomevelho = ""
quantidadeM = 0

for p in range(1, 5):
    print(f"--------Pessoa {p} ---------")
    nome = str(input("Digite seu nome: ")).capitalize()
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo F/M: ")).upper()

    idademedia += idade

    if sexo == "M":
        if p == 1:
            idadevelho = idade

        else:
            if idadevelho < idade:
                idadevelho = idade
                nomevelho = nome

    if sexo == "F" and idade < 20:
        quantidadeM += 1

print(f"A MÉDIA de idade do grupo é: {idademedia/4}")
print(f"O homen mais VELHO é o: {nomevelho} com idade de: {idadevelho} anos")
print(f"A quantidade de mulheres com MENOS DE 20 anos é: {quantidadeM}")
