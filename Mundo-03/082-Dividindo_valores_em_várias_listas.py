"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

l = []

while True:
    l.append(int(input("Digite um valor: ")))
    c = str(input("Continuar S/n: ")).strip().lower()[0]

    if c == "n":
        break

p = []
i = []

for v in l:

    if v % 2 == 0:
        p.append(v)

    else:
        i.append(v)

print(f"Você digitou a lista: {l}, os pares são: {p}, e os ímpares são: {i}")
