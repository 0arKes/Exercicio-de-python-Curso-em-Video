"""
Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""

frase = str(input("Digite sua frease: ")).lower().strip()
frase = frase.split()
tfrase = ''.join(frase)
rev = ''

for c in range(-1,(-1*len(tfrase))-1,-1):
    rev += tfrase[c]


print(f'A frase {tfrase}, invertida fica {rev}')

if tfrase == rev:
    print(f'A frase: {tfrase} pode formar um Palíndromo!')
else:
    print(f'A frase: {tfrase} NÃo pode formar um Palíndromo!')
