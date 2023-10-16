def metade(preco):
    return preco / 2


def dobro(preco):
    return preco*2


def aumentar(preco, taxa):
    d = (preco * taxa/100)
    return preco + d


def diminuir(preco, taxa):
    d = preco * taxa/100
    return preco - d

def Moedas(tmoeda='R$',num=0):
    return f"{tmoeda}{num:.2f}".replace(".",",")
