"""
Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

num = int(input("Digite um número: "))
cont = 0

for c in range(1,num+1):
    if num % c == 0:
        cont+=1
        print(f"O número {num} é divisivel por {c}")
if cont > 2:
    print(f"O número {num} não é primo")
else:
    print(f"O número {num} é primo")
