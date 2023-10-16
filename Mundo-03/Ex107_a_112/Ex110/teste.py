"""
Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
"""

#outros editores
import moedas

#pycharm
#from Ex107_a_112.Ex110 import moedas

valor = float(input("Digite o valor: "))

print(moedas.Resumo(10,15,valor))