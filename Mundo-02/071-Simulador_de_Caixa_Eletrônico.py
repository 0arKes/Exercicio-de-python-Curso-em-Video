"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print(40*"=")
valor = int(input("Qual valor para sacar: "))
print(40*"=")
notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0

while valor >= 1:

    if valor % 50 == 0:
        notas50 += 1
        valor -= 50

    elif valor % 20 == 0:
        notas20 += 1
        valor -= 20

    elif valor % 10 == 0:
        notas10 += 1
        valor -= 10

    else:
        notas1 += 1
        valor -= 1

print(f"[{notas50}] notas de R$ 50 \n[{notas20}] notas de R$20 \n[{notas10}] notas de R$10 \n[{notas1}] notas de R$1")
