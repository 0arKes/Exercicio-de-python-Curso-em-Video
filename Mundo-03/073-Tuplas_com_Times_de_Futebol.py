"""
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Santos."""

times = ("Botafogo","Palmeiras","Grêmio","Flamengo","Fluminense","Bragantino","Athletico-PR","Fortaleza","Atlético","Cuiabá","São Paulo","Cruzeiro","Corinthians","Internacional","Goiás","Bahia","Santos","Vasco","Coritiba","América-MG")

print(f"Os 5 primeiros times são {times[:5]}")
print()
print(f"Os 4 ultimos times são {times[-4:]}")
print()
print(f"OA: {sorted(times)}")
print()

for pos,t in enumerate(times):
    if t == "Santos":
        print(f"O Santos esta na Posição: {pos+1}º")