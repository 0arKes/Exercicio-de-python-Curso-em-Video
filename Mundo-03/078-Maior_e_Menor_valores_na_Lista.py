"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
"""

valores = []
for x in range(0,4):
    valores.append(int(input("Digite um valor: ")))

maior = max(valores)
menor = min(valores)

print(40*"-=")
print(f"Sua lista é: {valores}")
print(f"O MAIOR valor da lista foi: {maior} e esta na posição: {valores.index(maior)+1}")
print(f"O MENOR valor foi: {menor}, e esta na posição: {valores.index(menor)+1}")
print(40*"-=")


#Solução 2
'''
valores = []
for c in range (0,4):
    valores.append(int(input(f"Digite o {c}º valor: ")))

maior = 0
mpos = ""
menor = 0
menpos = ""

for pos,n in enumerate(valores):
    if pos == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
            mpos += str(pos)
        if n < menor:
            menor = n
            menpos += str(pos)

print(f"Sua lista é: {valores}")
print(f"o maior valor é: {maior} e apareceu na posição {mpos}")
print(f"e o menor valoré: {menor} e apareceu na posição {menpos}")
'''