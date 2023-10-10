"""
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))
ultimo = primeiro + 10 * razão

for c in range(primeiro,ultimo,razão):
    print(f"{c}", end='')
    print('->' if c != ultimo-razão else ' FIM!',end='')
