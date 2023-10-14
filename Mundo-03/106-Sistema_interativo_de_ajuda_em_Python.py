"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
"""

def consult(comando):
    print('\033[36m')
    return print(f'\033[32m{help(comando)}')
    

while True:
    print("\033[35m-="*40)
    c = str(input(f"\033[34m{'Digite um comando para consutar: ':>50}")).lower()
    print('\033[35m-='*40)

    if c == "fim":
        break
    else:
        consult(c)

print("Programa encerrado")