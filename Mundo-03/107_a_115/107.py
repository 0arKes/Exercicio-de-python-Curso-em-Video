from moedas import *

valor = float(input("Digite o valor: "))

print(f"A metade de {valor} é {moedas.metade(valor)}")
print(f"A dobro de {valor} é {moedas.dobro(valor)}")
print(f"10% a mais de {valor} é {moedas.aumentar(valor):.1f}")
print(f"13% a menos de {valor} é {moedas.diminuir(valor)}")