"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

list = [[], []]

for c in range(0,3):
    n = int(input("Digite um número: "))

    if n % 2 == 0:
        list[0].append(n)
    else:
        list[1].append(n)

list[0].sort()
list[1].sort()

print(f"Os numeros Pares são: {list[0]} e os Ímpares são: {list[1]}")