"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""


n1 = int(input("Digite o PRIMEIRO número: "))
n2 = int(input("Digite o SEGUNDO número: "))
n3 = int(input("Digite o TERCEIRO número: "))
n4 = int(input("Digite o QUARTO número: "))
t = (n1,n2,n3,n4)

v9 = 0
pri3 = 0
pares = ""

for pos,n in enumerate(t):
    if n == 9:
        v9 += 1

    if n == 3 and pri3 == 0:
        pri3 = pos

    if n % 2 == 0:
        pares += str(n) + ' '

print(f"O número 9 apareceu: {v9} vezes")
print(f"O primeiro 3 ta na posição: {pri3+1}" if pri3 != 0 else "Não houve números 3")
print(f"Os números pares são: {pares}")


#Solução 2
'''
n = (int(input("Digite o 1 valor: ")), int(input("Digite o 2 valor: ")), int(input("Digite o 3 valor: ")), int(input("Digite o 4 valor: ")))
print(20*"-=")
print(f"o numermo 9 apareceu {n.count(9)} vezes")

if 3 in n:
    print(f"a posição do primeiro 3 é a {n.index(3)+1}º")
else:
    print("Não houve numero 3")

print("os pares digitados são: ", end='')
for c in n:
    if c % 2 == 0:
        print(c,end=' ')
'''