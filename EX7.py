"""
Faça um programa que leia um número indeterminado de valores numéricos, encerrando
a entrada de dados quando for informado um valor igual a -1 (que não deve ser
armazenado). Após esta entrada de dados, faça:

• Mostre a quantidade de valores que foram lidos;
• Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
• Exiba todos os valores na ordem inversa à que foram informados, um ao lado do outro;
• Calcule e mostre a soma dos valores;
• Calcule e mostre a média dos valores;
• Calcule e mostre a quantidade de valores acima da média calculada;
"""
f = True
while f == True:
    lista = []
    cont = 0
    cont1 = 0

    while True:
        try:
            num = int(input("Digite um número para adicionar na lista: "))
            lista.append(num)
            cont += 1

            resp1 = input("Você quer adicionar um número? [S/N]: ").strip().upper()
            if resp1 == "N":
                break
        except ValueError:
            print("Erro de valor!")
        
    lista_reversa = lista[::-1]
    soma_lista = sum(lista)
    media_lista = soma_lista / len(lista)

    for num in lista:
        if num > media_lista:
            cont1 += 1

    print(f"\nQuantidade de números inseridos: {cont}")
    print(f"Lista: {lista}")
    print(f"Lista com ordem inversa: {lista_reversa}")
    print(f"Soma dos valores: {soma_lista}")
    print(f"Média dos valores: {media_lista}")
    print(f"Quantidade de valores acima da média: {cont1}")

    resp = input("\nQuer fazer outra lista com outros números? [S/N]: ").strip().upper()

    if resp == "N":
        f = False    