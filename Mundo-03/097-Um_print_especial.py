"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""

def Menssagen(txt):

    print(len(txt) * "~")
    print(txt)
    print(len(txt) * "~")

Menssagen("Boa noite")
Menssagen("olá Mundo 2")