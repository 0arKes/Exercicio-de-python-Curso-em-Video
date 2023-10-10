"""
Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

numero = int(input("Digite um número inteiro: "))
comando = int(input("1 para Binário, 2 para Octal ou 3 para hexadecimal: "))

if comando == 1:
    print(f"Em Binário o número {numero} é {bin(numero)}")
elif comando == 2:
    print(f"Em octal o número {numero} é {oct(numero)} ")
elif comando == 3:
    print(f"Em hexadecimal o número {numero} é {hex(numero)}")
else:
    print("\033[31mComando Inválido")