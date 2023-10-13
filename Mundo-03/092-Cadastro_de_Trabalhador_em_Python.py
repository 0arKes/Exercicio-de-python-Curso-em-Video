"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date

anoatual = date.today().year
dados = {}

dados["Nome"] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
dados["Idade"] = anoatual - nasc
dados["Carteira de Trab"] = int(input("Sua carteira/zero caso não tenha: "))

if dados["Carteira de Trab"] != 0:

    dados["Ano de contrato"] = int(input("Ano de contrato: "))
    dados["Salário"] = int(input("Salário: "))

    aposentar = ((anoatual - dados["Ano de contrato"]) - 30) * -1


    for k,v in dados.items():
        print(f"{k} = {v}")
    print(f"Você vai aposentar no ano {anoatual+aposentar}, com {dados['Idade']+aposentar}")