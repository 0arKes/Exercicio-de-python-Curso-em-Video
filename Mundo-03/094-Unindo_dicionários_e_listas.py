"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

pessoas = {}
cadastrados = []
mediaI = 0
mulheres = []
Maiores = []

while True:
    pessoas["Nome"] = str(input("Nome: "))
    pessoas["Sexo"] = str(input("M/F: "))
    pessoas["Idade"] = int(input("Idade: "))

    mediaI += pessoas["Idade"]

    cadastrados.append(pessoas.copy())
    r = str(input("Continuar S/N: "))
    if r == "n":
        break

print(f"A quantidade de registrados é: {len(cadastrados)}")
print(f"A media de idade do grupo é: {mediaI/len(cadastrados)}")

for i,v in enumerate(cadastrados):
    if cadastrados[i]["Sexo"] == "f":
        mulheres.append(cadastrados[i]["Nome"])
    if cadastrados[i]["Idade"] > 18:
        Maiores.append(cadastrados[i]["Nome"])

print(f"As mulheres são: {mulheres}")
print(f"Os maiores de idade: {Maiores}")