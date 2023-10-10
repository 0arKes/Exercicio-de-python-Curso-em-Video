from datetime import date

menores = int()
maiores = int()
ano = date.today().year

for c in range(1,8):
    nasc = int(input("Digite o ano de nascimento da {}º pessoa: ".format(c)))
    if ano - nasc >= 18:
        maiores +=1
    else:
        menores+=1
print("{} pessoas são maiores".format(maiores))
print("{} pessoas são menores".format(menores))
