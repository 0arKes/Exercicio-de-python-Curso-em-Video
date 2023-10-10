"""
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

r1 = int(input('Digite o PRIMEIRO segmento: '))
r2 = int(input('Digite o SEGUNDO segmento: '))
r3 = int(input('Digite o TERCEIRO segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    if r1 == r2 and r2 == r3:
        print(f'Os segmentos {r1}, {r2}, {r3}, formam um Triângulo EQUILÁTERO')
    elif r1 != r2 and r2 != r3:
        print(f'Os segmentos {r1}, {r2}, {r3}, formam um Triângulo ESCALENO')
    else:
        print(f'Os segmentos {r1}, {r2}, {r3}, formam um Triângulo ISÓSCELES')

else:
    print(f'Os segmentos {r1}, {r2}, {r3}, não forma um Triângulo')