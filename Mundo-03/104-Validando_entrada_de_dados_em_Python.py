"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""

def leaint(valor):
    ok = False

    while True:
        n = str(input(valor))

n = leaint("Digite: ")
print(n)