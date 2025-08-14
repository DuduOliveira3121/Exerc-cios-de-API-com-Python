"""
Álcool:
• até 20 litros: desconto de 3% por litro <--- == 20:
• acima de 20 litros: desconto de 5% por litro <--- > 20
Gasolina:
• até 20 litros: desconto de 4% por litro
• acima de 20 litros: desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado
da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litros = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Qual tipo? (A - álcool | G - Gasolina)").strip().upper()
total = 0

if tipo_combustivel == 'A' and litros == 20:
    desc3 = 1.90 * 0.03
    total = litros * (1.90 - desc3)
elif tipo_combustivel == 'A' and litros > 20:
    desc5 = 1.90 * 0.05
    total = litros * (1.90 - desc5)

elif tipo_combustivel == 'G' and litros == 20:
    desc4 = 1.90 * 0.04
    total = litros * (1.90 - desc4)
elif tipo_combustivel == 'G' and litros > 20:
    desc6 = 1.90 * 0.06
    total = litros * (1.90 - desc6)

print(f"Litros: {litros}")
print(f"Tipo de combustível: {tipo_combustivel}")
print(f"Total a pagar: {total}")
