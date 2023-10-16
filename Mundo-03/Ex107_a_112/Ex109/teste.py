from Ex107_a_115.Ex109 import moedas

valor = float(input("Digite o valor: "))

print(f"A metade de {moedas.Moedas(num=valor)} é {moedas.metade(valor, format=True)}")
print(f"A dobro de {moedas.Moedas(num=valor)} é {moedas.dobro(valor, format=True)}")
print(f"10% a mais de {moedas.Moedas(num=valor)} é {moedas.aumentar(valor,10, format=True)}")
print(f"13% a menos de {moedas.Moedas(num=valor)} é {moedas.diminuir(valor,13, format=True)}")