def sis(comando):
    print((comando))


while True:
    c = str(input("Digite um comando para consutar: "))
    if c == "fim":
        break
    else:
        sis(c)

print("Programa encerrado")