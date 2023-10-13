"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

aproveitamento = {}
aproveitamento["Nome"] = str(input("Nome: "))
partidas = int(input("Digite quantas partidas foram: "))
gol = []
totalg = 0
c = 0

while True:
    gol.append(int(input(f"Digite quantos gols teve o jogo {c}: ")))
    aproveitamento["gols"] = gol
    totalg += gol[c]
    c += 1

    if c == partidas:
        break

aproveitamento["total gol"] = totalg

for k,v in aproveitamento.items():
    print(f"O campo {k} tem valor {v}")

print(40*"=-")
print(f"O jogador {aproveitamento['Nome']} teve: ")
print()

for n in range(0, partidas):
    print(f"Na partida: {n} -- o jogador: {aproveitamento['Nome']} fez: {aproveitamento['gols'][n]}")
print()
print(f"Foi um total de: {totalg}")