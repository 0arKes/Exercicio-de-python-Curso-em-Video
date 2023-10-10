"""
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

valor = float(input("Digite o valor do produto: "))
metodo = int(input("[1] para a vista, \n"
                   "[2] a vista no cartao, \n"
                   "[3] 2x no cartao ou \n"
                   "[4] para 3x cartao: "))

if metodo == 1:
    print(f"Seu produto custará: R${valor-(valor*.1):.2f}")
elif metodo == 2:
    print(f"Seu produto custará: R${valor-(valor*.05):.2f}")
elif metodo == 3:
    print("Seu produto custará R$",valor)
elif metodo == 4:
    parcela = int(input("Quantas parcelas: "))
    print(f"O valor de {(valor*1.2/parcela):.2f} parcelas e o valor final é {valor*1.2:.2f}")
else:
    print('Comando Inválido')