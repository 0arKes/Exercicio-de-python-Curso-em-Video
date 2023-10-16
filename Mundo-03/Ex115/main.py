from Ex115 import Cadastro
from Ex115 import Cabecario
from time import sleep

dados = 'DADOS.txt'

if not Cadastro.verifica_arq(dados):
    Cadastro.ciartxt(dados)



while True:
    resp = Cabecario.menu(['Ver Pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do programa'])

    if resp == 1:
        Cadastro.LerCad(dados)

    elif resp == 2:
        Cadastro.CriarCad(dados)

    elif resp == 3:
        print('Até logo...')
        break

    else:
        print('\033[31mComando Inválido! Use umas das opções a seguir\033[m')

    sleep(2)