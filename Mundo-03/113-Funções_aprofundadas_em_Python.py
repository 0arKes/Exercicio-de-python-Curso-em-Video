"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leaint(valor):

    valor = input(valor)

    try:
        valor = int(valor)

    except:
        while valor.isnumeric() == False:
            print('\033[31mERRO! Digite apenas números\033[m')
            valor = input('Digite apenas números: ')

    else:
        return valor


n = leaint('Digite um número: ')
print(f'Você Digitou o número {n}')