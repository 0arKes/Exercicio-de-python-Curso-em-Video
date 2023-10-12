l = []

while True:
    l.append(int(input("Digite um valor: ")))
    c = str(input("Continuar: "))

    if c != "s":
        break
l.sort(reverse=True)
print(f"Sua Lista é {l}, vc digitou {len(l)} numeros")
print("ha 5" if 5 in l else "nao ha 5")