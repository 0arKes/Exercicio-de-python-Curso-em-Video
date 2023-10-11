"""
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

continuar = "s"
maiores = 0
quanthomens = 0
quantmulheres = 0

while continuar in "Ss":
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo M/F: ")).strip().lower()[0]

    while sexo != "m" and sexo != "f":
        sexo = str(input("Apenas M/F: "))

    if idade > 18:
        maiores += 1

    if sexo == "m":
        quanthomens += 1

    elif sexo == "f" and idade < 20:
        quantmulheres += 1

    print(20*"=")
    print("Registrando ...")
    print(20*"=")

    continuar = str(input("Quer continuar s/n: ")).lower().strip()[0]
    while continuar != "s" and continuar != "n":
        continuar =str(input("Apenas S/n: "))

    if continuar in "Nn":
        break

print(f"A quantidade de maiores é: {maiores}, e a quantidade de homens é: {quanthomens}, e a quantidade de Mulheres menores de 20 anos é: {quantmulheres}")