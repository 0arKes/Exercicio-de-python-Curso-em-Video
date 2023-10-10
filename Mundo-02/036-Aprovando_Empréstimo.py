"""
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valorC = int(input("Digite o valor da casa: "))
salario = int(input("Digite o valor do salário: "))
anos = int(input("Em quantos anos vc vai pagar: "))

pretação = valorC/(anos*12)

if pretação >= salario*0.3:
    print ("Você não pode pegar o empréstimo")
else:
    print(f"Você pode pegar o empréstimo e vai pagar {pretação} por {anos*12} meses")