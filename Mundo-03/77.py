palavras = ("aprender", "programar", "linguagem", "python", "curso", "praticar")

for p in palavras:
    print(f"\nA palavra {p} tem: ", end='')
    for letra in p:
        if letra in "aeiou":
            print(letra,end='')