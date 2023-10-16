"""
Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

#outros editores
from utilidades import moedas
from utilidades import dados

#pycharm
#from Ex107_a_112.Ex112.utilidades import moedas
#from Ex107_a_112.Ex112.utilidades import dados

v = dados.leiadado('Digite um valor: ')

print(moedas.Resumo(10,15, v))