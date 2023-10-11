"""
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

continuar = 'S'
valor = 0
contador = 0
Menor = 0
Maior = 0
soma = 0

while continuar == "S":
    valor = int(input("Digite um valor: "))
    contador += 1
    soma += valor

    if contador == 1:
        Maior = Menor = valor
    else:
        if valor > Maior:
            Maior = valor
        if valor < Menor:
            Menor = valor

    continuar = str(input("Vc quer continuar S/N: ")).strip().upper()[0]

print(f"A razão entre os números digitados é: {soma/contador} e o maior número foi: {Maior} e o menor foi: {Menor}")
