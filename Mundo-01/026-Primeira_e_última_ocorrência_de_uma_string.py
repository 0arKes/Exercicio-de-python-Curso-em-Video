"""
Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

frase = str(input('Digite uma frase: ')).strip()
print(f'Sua frase é: {frase}')
print(f'Sua frase tem {frase.lower().count("a")} letra(s) "A",\nela aparece na primeira vez na posição: {frase.lower().find("a")+1},\ne aparece em {frase.lower().rfind("a")+1} pela ultima vez [Considerando espaços]')
