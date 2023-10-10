
pesoMaior = 0.0
pesoMenor = 0.0

for c in range(1,6):
    pesoGeral = float(input("Digite o peso da {}º pessoa: ".format(c)))
    if c == 1:
        pesoMaior = pesoGeral
        pesoMenor = pesoGeral

    else:
        if pesoGeral > pesoMaior:
            pesoMaior = pesoGeral
        elif pesoGeral < pesoMenor:
            pesoMenor = pesoGeral

print ("o maior peso foi {} e o menor foi {}".format(pesoMaior,pesoMenor))