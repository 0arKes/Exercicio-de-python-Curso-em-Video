def leaint(valor):
    valor = input(valor)

    try:
        valor = int(valor)

    except:
        while valor.isnumeric() == False:
            print('\033[31mERRO! Digite apenas números\033[m')
            valor = input('Digite apenas números: ')

    else:
        return valor


def linha():
    return '-' * 50


def cabeçario(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista:list):
    cabeçario('SISTEMA DE CADASTRO')
    c = 1

    for i in lista:
        print(f'{c} -> {i}')
        c += 1

    print(linha())
    r = leaint('')
    return r