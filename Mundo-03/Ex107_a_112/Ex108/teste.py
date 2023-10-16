"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
"""

#outros editores
import moedas

#pycharm
#from Ex107_a_115.Ex108 import moedas

valor = float(input("Digite o valor: "))

print(f"A metade de {moedas.Moedas(num=valor)} é: {moedas.Moedas(num=moedas.metade(valor))}")
print(f"A dobro de {moedas.Moedas(num=valor)} é: {moedas.Moedas(num=moedas.dobro(valor))}")
print(f"10% a mais de {moedas.Moedas(num=valor)} é: {moedas.Moedas(num=moedas.aumentar(valor, 10))}")
print(f"13% a menos de {moedas.Moedas(num=valor)} é: {moedas.Moedas(num=moedas.diminuir(valor, 13))}")