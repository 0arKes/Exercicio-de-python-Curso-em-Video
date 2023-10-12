"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

l = []

for c in range(0,5):
    num = int(input("Digite um número: "))

    if c == 0 or l[-1] < num:
        l.append(num)

    else:
        cont = 0
        while cont <= len(l):
            if num <= l[cont]:
                l.insert(cont,num)
                break
            cont += 1
print(l)