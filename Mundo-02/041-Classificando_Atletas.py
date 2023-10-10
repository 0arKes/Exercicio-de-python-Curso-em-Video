"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""


from datetime import date

nasc = int(input("Digite o ano do seu nascimento:  "))
ano = date.today().year - nasc

if ano < 9:
    print("Categoria Mirim")
elif ano < 14:
    print("Categoria Infantil")
elif ano < 19:
    print("Categoria júnior")
elif ano < 20:
    print("Categoria Sênior")
else:
    print("Categoria Master")