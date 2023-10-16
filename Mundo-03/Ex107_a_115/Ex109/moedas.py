def metade(moedas=0, format=False):
    if format == True:
        return Moedas(num=moedas/2)
    else:
        return moedas / 2


def dobro(moedas, format=False):
    if format:
        return Moedas(num=moedas*2)
    else:
        return moedas*2


def aumentar(moedas, taxa, format=False):
    if format:
        return Moedas(num=(moedas * (taxa/100)) + moedas)
    else:
        return (moedas * (taxa/100)) + moedas


def diminuir(moedas, taxa, format=False):
    d = moedas * (taxa/100)

    if format:
        return Moedas(num=moedas-d)
    else:
        return moedas - d


def Moedas(tmoeda='R$',num=0.0):
    return f"{tmoeda}{num:.2f}".replace(".",",")
