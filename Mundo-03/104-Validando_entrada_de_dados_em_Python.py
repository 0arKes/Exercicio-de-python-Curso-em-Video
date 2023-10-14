"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""

def leaint(valor):
    valor = input(valor)

    if valor.isnumeric() == True:
        valor = int(valor)

    else:
        while valor.isnumeric() == False:
            print('\033[31mERRO! Digite apenas números')
            valor = input('\033[37mDigite apenas números: ')
    
    return valor

n = leaint('Digite um numero: ')
print(f'Você Digitou o número {n}')