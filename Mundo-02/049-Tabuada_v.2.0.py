"""
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

tab = int(input("Digite qual número você quer ver a tabuada: "))

for c in range(1,11):
    print("{}x{} = {}".format(c,tab,tab*c))