'''Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

• Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
• Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
• A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere
o programa permitindo que o usuário digite o salário inicial do funcionário.'''

# salario exemplo

'''
sal = 1.000
ano_atual = 2025
ano_inicial = 1995
porc_ano_2 = 1.5

for i in range(2, ano_atual - ano_inicial):
    porc_ano_2 = porc_ano_2 / 100
    sal += sal * porc_ano_2
    porc_ano_2 = porc_ano_2 * 100
    porc_ano_2 = porc_ano_2 * 2

print(f'O salário atual é: {sal:.2f}')
'''

# com salario e ano dito pelo usuário
while True:
    try:
        sal = float(input('Digite o salário inicial:'))
        break
    except ValueError:
        print("Entrada inválida! Digite apenas números.")

while True:
    try:
        ano_inicial = int(input('Digite o ano inicial: '))
        break
    except ValueError:
        print("Entrada inválida! Digite apenas números.")

ano_atual = 2025
porc = 1.5

for i in range((ano_atual - ano_inicial) - 1):
    porc = porc / 100
    sal += sal * porc
    porc = porc * 100
    porc = porc * 2

print(f'O salário atual é: {sal:.2f}')