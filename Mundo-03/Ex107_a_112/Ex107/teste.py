"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
"""
#outros editores
import moedas

#pycharm
#from Ex107_a_115.Ex107 import moedas
valor = float(input("Digite o valor: "))

print(f"A metade de {valor} é: {moedas.metade(valor)}R$")
print(f"A dobro de {valor} é: {moedas.dobro(valor)}R$")
print(f"10% a mais de {valor} é: R${moedas.aumentar(valor, 10):.2f}")
print(f"13% a menos de {valor} é R${moedas.diminuir(valor, 13):.2f}")
