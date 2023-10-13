"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

def voto(idade):
    from datetime import date
    idade = date.today().year - idade

    if idade < 18:
        return print(f"Você tem {idade}: não pode votar")
    elif idade >= 18 and idade < 65:
        return print(f"Você tem {idade}: voto obrigatorio")
    elif idade >= 65:
        return print(f"Você tem {idade}: voto opcional")


voto(int(input("Digite o ano de nascimento: ")))