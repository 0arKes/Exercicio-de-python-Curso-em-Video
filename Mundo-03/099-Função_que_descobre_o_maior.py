"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*l):
    print(f"Você digitou {len(l)} números e o maior é {max(l)}")

maior(4,3,6,8,23,1,3,7,84,3)
maior(3,5,677,3,1,3,3,33,567,)
maior(3,2,1)
