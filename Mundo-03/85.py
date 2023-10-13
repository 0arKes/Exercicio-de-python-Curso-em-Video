list = [[], []]

for c in range(0,3):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        list[0].append(n)
    else:
        list[1].append(n)
list[0].sort()
list[1].sort()
print(list)
print(f"Os numeros pares são {list[0]} e os impares são {list[1]}")