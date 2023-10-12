"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
"""

lista = []
while True:
    valor = int(input("Digite um valor: "))
    if valor in lista:
        print(f"O valor {valor} já esta na lista, tente outro")
    else:
        lista.append(valor)
        print(f"O valor {valor} foi adcionado")
    c = str(input("Quer continuar ? S/n ")).strip().lower()[0]
    if c == "n":
        break

print(f"Sua lista é {sorted(lista)}")
