"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

st = str(input("Digite sua expressão: "))
l = []
pa = 0


for c in st:
    l.append(c)

for x in l:

    if x == "(":
        pa +=1

    elif x == ")":
        pa -=1

if pa == 0:
    print("A expressão esta correta!")
else:
    print("A expressão esta INcorreta")