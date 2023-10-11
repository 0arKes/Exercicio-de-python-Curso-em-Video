"""
Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""

contador = soma = 0
while True:
    n = int(input("Digite um Número [999 para parar]: "))
    
    if n == 999:
        break

    soma += n
    contador +=1

print(f"Você digitou: {contador} número(s) e a soma entre eles foi de: {soma}")