#Solução com bibliotéca math

from math import hypot
cat_o = float(input('Comprimento do Cateto Oposto: '))
cat_a = float(input('Comprimento do Cateto Adacente: '))
h = hypot(cat_a, cat_o)
print(f'A hipotenusa mede {h:.2f}')

#Solução com python
'''
cat_o = float(input('Comprimento do Cateto Oposto: '))
cat_a = float(input('Comprimento do Cateto Adacente: '))
h = (cat_a**2+cat_o**2) ** (1/2)
print(f'A hipotenusa mede {h:.2f}')
'''