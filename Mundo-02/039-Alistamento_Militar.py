"""
Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

anoatual = date.today().year

nasc = int(input("Digite o ano que você nasceu: "))

if anoatual-nasc > 18:
    print(f"Você já deveria ter se alistado, no ano {(anoatual - ((anoatual-nasc)-18))}")
elif anoatual-nasc == 18:
    print("Você deve se alistar esse ano")
else:
    print(f"Você terá que se alistar no ano {((18 - (anoatual-nasc)) + anoatual)}")