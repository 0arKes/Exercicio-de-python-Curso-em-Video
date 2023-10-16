def verifica_arq(arq):
    try:
        txt = open(arq, 'rt')
        txt.close()

    except:
        return False

    else:
        return True


def ciartxt(arq):
    try:
        txt = open(arq, 'wt+')
        txt.close()

    except:
        print('\033[31mImpossivel Criar o arquivo. Tente mover o programa para um disco que seu usuário tenha acesso')

    else:
        print('\033[34mArquivo criado na raiz com sucesso!')


def CriarCad(arq):
    nome = str(input("Nome: ")).strip().capitalize()
    idade = str(input("Idade: ")).strip()

    try:
        file = open(arq, 'at')
        file.write(f'{nome}/{idade}\n')
    except:
        print('\033[31mImpossivel cadastrar!\033[m')

    else:
        print('\033[36mRegistrado com sucesso!\033[m')
        f.close()


def LerCad(arq):

    try:
        file = open(arq, 'rt')

    except:
        print('\033[31mArquivo apagado ou obstruido\033[m')

    else:
        for linha in file:
            dado_c = linha.split('/')
            dado_c[1] = dado_c[1].replace('\n', '')
            print(f'{dado_c[0]:<30}{dado_c[1]:>3} anos')

    finally:
        file.close()