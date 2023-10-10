
idademedia = 0
idadevelho = 0
nomevelho = ""
quantidadeM = 0

for p in range(1, 3):
    print("--------Pessoa {} ---------".format(p))
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo F/M: "))

    idademedia += idade

    if sexo == "M":
        if p == 1:
            idadevelho = idade

        else:
            if idadevelho < idade:
                idadevelho = idade
                nomevelho = nome

    if sexo == "F" and idade < 20:
        quantidadeM += 1

print("a MEDIA de idade do grupo é {}".format(idade/2))
print("o homen mais VELHO é o {} com idade de {} anos".format(nomevelho,idadevelho))
print("a quantidade de mulheres com MENOS DE 20 anos é {}".format(quantidadeM))
##
#print(quantidadeM)
#print(idadevelho, nomevelho)
#print(idademedia/2)
