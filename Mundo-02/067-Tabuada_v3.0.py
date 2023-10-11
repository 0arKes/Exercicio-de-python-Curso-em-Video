"""
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
"""

contador = 1

while True:
    num = int(input("Digite um número para ver sua tabuada: "))

    if num < 0:
        print("Valor Negativo")
        break

    print(20*"-")

    while contador <= 10:
        print(f"{num}x{contador}={num*contador}")
        contador += 1

    contador = 1
    print(20*"-")
