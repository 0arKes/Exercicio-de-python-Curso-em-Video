"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

jogador = {}
capionato = []
gols = []
totgol = 0
contador = 0

while True:
    jogador["Nome"] = str(input("Nome: "))
    quantjogos = int(input(f"{jogador['Nome']} Jogou quantos jogos: "))

    while contador < quantjogos:
        gols.append(int(input(f"No jogo {contador}: ")))
        totgol += gols[contador]
        contador += 1

    jogador["Gols"] = gols[:]
    jogador["Total"] = totgol
    capionato.append(jogador.copy())
    gols.clear()
    contador = 0
    totgol = 0

    r = str(input("Continuar s/n: ")).strip().lower()[0]
    if r == "n":
        break

print()
print(f'{"id":>5}{"Nome":>15}{"Gols":>15}{"TOTAL":>15}')

for c,v in enumerate(capionato):
    print(f'{c:>5}', end='')
    print(f"{capionato[c]['Nome']:>16}", end='')
    print(f"{str(capionato[c]['Gols']):>12}", end='')
    print(f"{capionato[c]['Total']:>12}", end= '')
    print()

while True:
    ld = int(input("Levanta dados de qual jogador [999 Break] ?"))
    
    if ld == 999:
        break
    else:
        print(capionato[ld])

print("Programa encerrado")