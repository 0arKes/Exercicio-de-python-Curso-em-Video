"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

V1 = int(input("Digide o PRIMEIRO valor: "))
V2 = int(input("Digite o SEGUNDO valor: "))
menu = 0
verificador = True

while verificador == True:
    menu = int(input("""    [1]Somar
    [2]Multiplicar
    [3]Qual é maior
    [4]Novos números
    [5]Sair
    """))

    print()

    if menu == 1:
        print(f"{V1}+{V2}={V1+V2}")

    elif menu == 2:
        print(f"{V1}x{V2}={V1*V2}")

    elif menu == 3:
        if V1>V2:
            print(f"{V1}>{V2}")

        elif V1<V2:
            print(f"{V2}>{V1}")

        else:
            print("São iguais")

    elif menu == 4:
        V1 = int(input("Digite o novo PRIMEIRO número: "))
        V2 = int(input("Digite o novo SEGUNDO número: "))

    elif menu == 5:
        verificador = False

    else:
        print("Comando INVÁLIDO, tente novamente...")
    
    print()

print("Fim do programa")
