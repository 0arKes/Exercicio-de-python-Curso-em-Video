"""
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

IMC = peso/(altura**2)
print (IMC)

if IMC < 18.5:
    print(f"IMC = {IMC} Abaixo do Normal")
elif IMC < 25:
    print(f"IMC = {IMC} Normal")
elif IMC < 30:
    print(f"IMC = {IMC} Sobrepeso")
elif IMC < 40:
    print(f"IMC = {IMC} Obesidade")
else:
    print(f"IMC = {IMC} Obesidade Mórbida")