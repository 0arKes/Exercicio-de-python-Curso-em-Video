matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = 0
soma3 = 0
maior = 0

for c in range(0,3):
    for l in range(0,3):
        matriz[c][l] = int(input(f"Digite um valor para [{c} {l}]: "))


print()
for c in range(0,3):
    for l in range(0,3):
        print(f"[{matriz[c][l]}]",end='')

        if matriz[c][l] % 2 == 0:
            pares += matriz[c][l]

    print()

soma3 += matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f"A soma dos valores pares é {pares}")
print(f"A soma da terceira coluna é {soma3}")

maior = matriz[1][0]

if maior < matriz[1][1]:
    maior = matriz[1][1]

if maior < matriz[1][2]:
    maior = matriz[1][2]

print(f"O maior item da linha dois é {maior}")

