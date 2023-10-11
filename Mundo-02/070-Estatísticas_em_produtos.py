"""
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """

continuar = "s"
total = 0
maismil = 0
menorvalor = 0
contador = 0
nomedomaisbarato = ""


while continuar == "s":
    nomep = str(input("Nome do Produto: "))
    valorp = int(input("Valor do Produto: "))

    total += valorp
    contador += 1

    if valorp > 1000:
        maismil += 1

    if contador == 1:
        menorvalor = valorp
        nomedomaisbarato = nomep

    else:
        if valorp < menorvalor:
            menorvalor = valorp
            nomedomaisbarato = nomep


    continuar = str(input("Quer continuar s/n: ")).strip().lower()[0]

print(20*"=")
print(f"Você comprou {contador} produtos \n"
      f"O valor total é de R${total}\n"
      f"E {maismil} são produtos acima de R$1000\n"
      f"O produto mais barato foi {nomedomaisbarato} por R${menorvalor}")
