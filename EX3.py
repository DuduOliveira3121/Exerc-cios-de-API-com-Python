"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:

Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero e

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for
D ou E.
"""
comecar = True
while comecar == True:

    f1 = True
    while f1 == True:
        try:
            nota_parcial1 = float(input("Digite a 1ª nota parcial: "))
            f1 = False
        except ValueError:
            print("Valor incorreto!")

    f2 = True
    while f2 == True:
        try:
            nota_parcial2 = float(input("Digite a 2ª nota parcial: "))
            f2 = False
        except ValueError:
            print("Valor incorreto!")
    

    media = (nota_parcial1 + nota_parcial2) / 2

    if media >= 9.0 and media <= 10.0:
        print("A")
        print(f"Média: {media}")
        print("APROVADO")

    elif media >= 7.5 and media <= 9.0:
        print("B")
        print(f"Média: {media}")
        print("APROVADO")

    elif media >= 6.0 and media <= 7.5:
        print("C")
        print(f"Média: {media}")
        print("APROVADO")

    elif media >= 4.0 and media <= 6.0:
        print("D")
        print(f"Média: {media}")
        print("REPROVADO")

    elif media >= 0 and media <= 4.0:
        print("E")
        print(f"Média: {media}")
        print("REPROVADO")

    resp = input("Quer inserir outras notas? [S|N]: ").strip().upper()
    if resp == "N":
        comecar = False
