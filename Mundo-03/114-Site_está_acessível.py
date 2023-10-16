"""
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import requests

try:
    url = 'http://pudim.com.br'
    requests.get(url, timeout=9)
    print("\033[34mEstá funcionando")
except:
    print("\033[31mEstá fora do ar")

