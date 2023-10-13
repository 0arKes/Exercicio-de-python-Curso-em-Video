"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

l = []

while True:
    l.append(int(input("Digite um valor: ")))
    c = str(input("Continuar S/n: ")).strip().lower()[0]

    if c != "s":
        break

l.sort(reverse=True)
print(f"Sua Lista é {l}, você digitou {len(l)} números")
print("Há 5" if 5 in l else "Não há 5")
