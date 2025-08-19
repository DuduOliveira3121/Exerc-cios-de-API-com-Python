"""
Desenvolver um programa para verificar a nota dos alunos em uma prova com 10
questões. O programa deve seguir os seguintes passos:

• Perguntar ao aluno a resposta de cada uma das 10 questões.
• Comparar as respostas fornecidas pelo aluno com o gabarito da prova.
• Calcular o total de acertos, atribuindo 1 ponto para cada resposta correta.
• Após cada aluno utilizar o sistema, perguntar se outro aluno deseja fazer a prova.
Após todos os alunos terem respondido, o programa deve informar:
• O maior e o menor número de acertos entre os alunos.
• O total de alunos que utilizaram o sistema.
• A média das notas da turma.
"""
alunos = []
prova_gabarito = ['c', 'd', 'a', 'b', 'e', 'a', 'c', 'b', 'd', 'e']
verdade = True
alunos.append(0)
al = 0

while verdade:
    for i in range(10):
        resposta = input(f'Digite a resposta da questão {(i+1)} (Ex: a): ')
        while resposta not in ["a", "b", "c", "d", "e"]:
            print("Valor errado")
            resposta = input(f'Digite a resposta da questão {(i+1)} (Ex: a): ')

        if prova_gabarito[i] == resposta:
            alunos[al] += 1

    pergunta = input('Outro aluno deseja fazer a prova?(S - sim ou N -não): ').strip().upper()
    while resposta not in ["S", "N"]:
            print("Valor errado")
            resposta = input(f'Outro aluno deseja fazer a prova?(S - sim ou N -não): ').strip().upper()
    if pergunta == 'N':
        alunos.append(0)
        verdade = False
        maior = 0
        menor = 0
        soma = 0
        tam_lista = len(alunos)
        for i in range(0,tam_lista -1):
            if alunos[i]>alunos[i+1] and alunos[i] > maior:
                maior = alunos[i]
            elif alunos[i+1] > maior:
                maior = alunos[i+1]
        for i in range(0, tam_lista-2):
            if alunos[i]<alunos[i+1] and alunos[i] < menor:
                menor = alunos[i]                               
            elif alunos[i+1] < menor:
                menor = alunos[i+1]
        menor = alunos[tam_lista-2]
        for i in range(0, tam_lista-1):
            soma += alunos[i]
        media = soma / (tam_lista-1)
        print('____________________________________')
        print(f'O maior número de acertos é {maior}')
        print(f'O menor número de acertos é {menor}')
        print(f'O total de alunos que usaram o sistema: {tam_lista-1}')
        print(f'O média das notas é {media:.2f}')
    else:
        alunos.append(0)
        al += 1