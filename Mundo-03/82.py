l = []
while True:
    l.append(int(input("Digite um valor: ")))
    c = str(input("continuar s/n: "))
    if c == "n":
        break
p = []
i = []
for v in l:
    if v % 2 == 0:
        p.append(v)
    else:
        i.append(v)

print(f"vc digitou a lista {l}, os pares são {p}, e os impares são {i}")