"""
Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

n_extenso = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorse","quize","dezesseis","dezessete","dezoito","dezenove","vinte")

n = 0

while True:
    n = int(input("Digite um número: "))
    if n >= 0 and n <= 20:
        print(f"Você digitou o número {n_extenso[n]}")
