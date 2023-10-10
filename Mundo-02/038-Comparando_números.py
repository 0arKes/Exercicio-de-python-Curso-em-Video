"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
"""

num1 = int(input("Digite o Primeiro número: "))
num2 = int(input("Digite o Segundo número: "))

if num1 > num2:
    print("O PRIMEIRO número é maior")
elif num1 < num2:
    print("O SEGUNDO número é maior")
else:
    print("Os números são IGUAIS")