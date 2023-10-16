"""
Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""

#outros editores
from utilidades import moedas

#pycharm
#from Ex107_a_112.Ex111.utilidades import moedas

valor = float(input("Digite o valor: "))

print(moedas.Resumo(10,15,valor))