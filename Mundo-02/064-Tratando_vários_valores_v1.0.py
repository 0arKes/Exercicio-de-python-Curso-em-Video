"""
Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

esc = 0
soma = 0
nd = 0

while esc != 999:
    esc = int(input(f"Digite o {nd+1}º número / 999 para parar o programa: "))
    if esc != 999:
        ultimo = esc
        soma += esc
        nd += 1

print(f"A Soma dos números digitados foi: {soma}, e a quanidade de numeros digitados é: {nd}")