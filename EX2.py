"""
Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a
valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas
disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo
de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes
na máquina.

• Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;

• Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma
nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
comecar = True
while comecar == True:

    valor_saque = 0

    f1 = True
    while f1 == True:
        try:
            valor_saque = int(input("Digite o valor do saque (Min: R$10 | Max: R$600): "))
            f1 = False
        except ValueError:
            print("Valor incorreto!")


    while valor_saque < 10 or valor_saque > 600:
        print("Valor inválido")
        valor_saque = int(input("Digite o valor do saque (Min: R$10 | Max: R$600): "))

    print("Este caixa apenas terá notas com o valor de 1, 5, 10, 50 e 100.")


    # Exemplo 256
    divisao1 = valor_saque // 100 # 256 / 100 = 2 ---> Duas notas de 100
    resto1 = valor_saque % 100 #56

    divisao2 = resto1 // 50 # 56 / 50 = 1 ---> Uma nota de 50
    resto2 = resto1 % 50 # 6

    divisao3 = resto2 // 10 # 6 / 10 = 0 ---> 0 notas de 10
    resto3 = resto2 % 10 # 6

    divisao4 = resto3 // 5 # 6 / 10 = 1,5 ---> Uma nota de 5
    resto4 = resto3 % 5 # 1

    divisao5 = resto4 // 1 # 1 / 1 = 1 ---> Uma nota de 1

    print(f"Quantidade de notas de 100: {divisao1}")
    print(f"Quantidade de notas de 50: {divisao2}")
    print(f"Quantidade de notas de 10: {divisao3}")
    print(f"Quantidade de notas de 5: {divisao4}")
    print(f"Quantidade de notas de 1: {divisao5}")

    resp = input("Deseja sacar outro valor? [S|N]? - ").strip().upper()
    
    if resp == "N":
        comecar = False