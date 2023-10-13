"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

np = []
pessoas = []
maisp = 0
menosp = 0

while True:
    np.append(str(input("Nome: ")))
    np.append(float(input("Peso: ")))

    if len(pessoas) == 0:
        maisp = menosp = np[1]

    else:
        if maisp < np[1]:
            maisp = np[1]

        if menosp > np[1]:
            menosp = np[1]

    pessoas.append(np[:])
    np.clear()

    c = str(input("Quer Continuar S/n: "))
    if c == "n":
        break

print(40*'-=')
print(f"A quantidade de pessoas registradas é: {len(pessoas)}")
print(f"A(s) pessoa(s) mais pesada tem: {maisp}Kg e é(são): ",end='')

for p in pessoas:
    if p[1] == maisp:
        print(f'{p[0]}, ', end='')

print()

print(f"E a(s) pessoa(s) mais leve tem: {menosp}Kg, e é(são): ",end='')

for p in pessoas:
    if p[1] == menosp:
        print(f'{p[0]}, ', end='')