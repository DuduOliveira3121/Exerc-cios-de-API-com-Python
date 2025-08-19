'''O cardápio de uma lanchonete é o seguinte:

Especificação   Código   Preço

Cachorro Quente 100      R$ 1,20
Bauru Simples   101      R$ 1,30
Bauru com ovo   102      R$ 1,50
Hambúrguer      103      R$ 1,20
Cheeseburguer   104      R$ 1,30
Refrigerante    105      R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule
e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

cardapio = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
itens_pedidos = {'100': 0,
                 '101': 0,
                 '102': 0,
                 '103': 0,
                 '104': 0,
                 '105': 0,
}
pedido = True
preço_total = 0

while pedido:
    cod = int(input('Digite o código do item:'))
    qtd = int(input('Digite a quantidade:'))
    
    if cod == 100:
        preço_total += cardapio[0] * qtd
        itens_pedidos['100'] += qtd
    elif cod == 101:
        preço_total += cardapio[1] * qtd
        itens_pedidos['101'] += qtd
    elif cod == 102:
        preço_total += cardapio[2] * qtd
        itens_pedidos['102'] += qtd
    elif cod == 103:
        preço_total += cardapio[3] * qtd
        itens_pedidos['103'] += qtd
    elif cod == 104:
        preço_total += cardapio[4] * qtd
        itens_pedidos['104'] += qtd
    else:
        preço_total += cardapio[5] * qtd
        itens_pedidos['105'] += qtd

    resp = input('Deseja pedir mais algo? (S -Sim ou N - Não)').strip().upper()
    while resp not in ["S", "N"]:
            print("Valor errado")
            resp = input('Deseja pedir mais algo? (S -Sim ou N - Não)').strip().upper()
    if resp == 'N':
        pedido = False
        for cod, quant in itens_pedidos.items():
            if quant >= 1:
                if cod == '100':
                    print(f'{quant} item nº {cod}: {(quant * cardapio[0]):.2f}')
                elif cod == '101':
                    print(f'{quant} item nº {cod}: {(quant * cardapio[1]):.2f}')
                elif cod == '102':
                    print(f'{quant} item nº {cod}: {(quant * cardapio[2]):.2f}')
                elif cod == '103':
                    print(f'{quant} item nº {cod}: {(quant * cardapio[3]):.2f}')
                elif cod == '104':
                    print(f'{quant} item nº {cod}: {(quant * cardapio[4]):.2f}')
                else:
                    print(f'{quant} item nº {cod}: {(quant * cardapio[5]):.2f}')
        print(f'Total do pedido: {preço_total:.2f}')