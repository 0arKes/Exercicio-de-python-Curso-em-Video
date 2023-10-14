"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(*nota,sti=False):
    
    """
    função que imprime nota dos alunos atravéz de um dict.

    :param nota: Recebe mútiplos valores (de notas)
    :param sti: Parâmetro opcional (padrão = False). Quando verdadeiro retorna a situação do aluno (boa/razoavel/ruim)
    :return:
    """

    media = 0
    dc = dict()
    dc["Nota"] = nota

    for n in nota:
        media += n
    media = media/len(nota)

    dc["média"] = media

    if sti == True:
        if media > 7:
            print("A média está BOA")
        elif media < 7 and media > 6:
            print("A média está RAZOAVEL")
        elif media < 6:
            print("A média está RUIM")

    return print(f"Quantidade de nota obtidas: [{len(dc['Nota'])}], Maior nota: [{max(dc['Nota'])}], Menor nota: [{min(dc['Nota'])}], M: [{dc['média']}], ", end='')


print(notas(9, 4, 6, 7, sti=True))