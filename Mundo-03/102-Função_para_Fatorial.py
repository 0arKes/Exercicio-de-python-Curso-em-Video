"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial (num, show=False):
    """
    Função para calculo de fatorial
    :param num: numero para visualizar o fatorial
    :param show: parametro que motra o fatorial ou não
    :return: retorna o valor obtido pelo calculo de fatorial
    """
    fat = 1
    while num > 0:
        fat *= num
        if show == True:
            print(f"{num}",end='')
            print(" x " if num != 1 else " = ",end='')
        num -= 1
    return fat


print(fatorial(10,True))
print(help(fatorial))