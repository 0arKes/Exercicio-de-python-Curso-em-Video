"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ("aprender", "programar", "linguagem", "python", "curso", "praticar")

for p in palavras:
    print(f"\nA palavra {p} tem: ", end='')

    for letra in p:
        if letra in "aeiou":
            print(letra, end=' ')