"""
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

p = int(input("Digite o PRIMEIRO termo: "))
r = int(input("Digite a RAZÃO: "))
e = 10

termo10 = p + (r * 10)


while p < termo10:
    print(f"[{p}]", end='')
    print("->"if p < (termo10-r) else "", end='')
    p += r

escolha = 1
cont = 0

print()

while escolha != 0:
    escolha = int(input("[0] para o programa ou qualquer número para continuar a PA: "))
    while cont < escolha:
        print("[{}]".format(p), end='')
        print("->" if cont < escolha else "", end='')
        p += r
        cont += 1
        e += 1

    cont = 0
    print()

print(f'O programa exibiu {e} números')