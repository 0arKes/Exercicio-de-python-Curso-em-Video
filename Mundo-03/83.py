st = str(input("Digite sua expressão: "))
l = []

pa = 0


for c in st:
    l.append(c)

for x in l:
    if x == "(":
        pa +=1
    elif x == ")":
        pa -=1

if pa == 0:
    print("a expressão esta correta!")
else:
    print("a expressão esta INcorreta")