alunos = []
media = 0

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("N1: "))
    nota2 = float(input("N2: "))
    media = (nota1+nota1) /2
    alunos.append([nome, [nota1,nota2],media])

    c = str(input("Continuar s/n: "))
    if c == "n":
        break
for a in alunos:
    print(a[0] , "     ", a[2])

