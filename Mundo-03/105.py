def notas(*nota,sti=False):
    media = 0
    dc = dict()
    dc["Nota"] = nota

    for n in nota:
        media += n
    media = media/len(nota)
    print(f"Quant nota {len(dc['Nota'])}, Maior {max(dc['Nota'])}, Menor {min(dc['Nota'])}, M: {media}, ",end='')

    if sti == True:
        if media > 7:
            print("A media esta boa")
        elif media < 7 and media > 6:
            print("A media ta razoavel")
        elif media < 6:
            print("A media esta ruim")

print(notas(9,4,6,7,sti=True))