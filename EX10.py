"""
Faça um programa para motoristas do Uber que, ao inserir o CEP do endereço do
destino do passageiro ele retorne qual região de São Paulo aquele CEP é. Utilize a
documentação: https://viacep.com.br/ ---> https://viacep.com.br/ws/"01234567"/json/

Exemplo: ao inserir o CEP 02122050 o resultado deve ser a mensagem: Bairro: Vila Maria
Alta, Zona Norte de São Paulo.
As zonas de São Paulo são: Norte, Sul, Leste, Oeste e Centro (indique também quando o
destino da corrida é pra fora da grande são paulo, em cidades vizinhas). Esse programa
será muito útil em relação à segurança dos motoristas, e com ele eles irão poder escolher
pra qual destino querem ou não aceitar corridas.
"""

# Observação 1 - A URL que está no exercício não estava funcionando. Tive que ir no site no navegador
# de forma normal para conseguir outro link

import requests
f = True
while f == True:

    flag = True
    while flag == True:
        try:
            cep = str(input("Digite somente com números o seu CEP: "))
            if len(cep) == 8:
                break
            print("Digite novamente o CEP!")
        except ValueError:
            print("Erro ao processar o CEP")
        
    CEP = (f"{cep[:5]}-{cep[5:]}")
                
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    data = response.json()

    localidade = data['localidade']
    bairro = data['bairro']
    prefixo_cep = cep[0:2]

    if localidade != "São Paulo":
        print("Destino da corrida: Fora da Grande São Paulo")
    else:
        if prefixo_cep == "01":
            zona = "Região Centro"
        elif prefixo_cep == "02":
            zona = "Zona Norte"
        elif prefixo_cep == "03":
            zona = "Zona Leste"
        elif prefixo_cep == "04":
            zona = "Zona Sul"
        elif prefixo_cep == "05":
            zona = "Zona Oeste"
            
        print(f"Bairro: {bairro}, {zona} de São Paulo")
    
    resp = input("Quer inserir outra sigla? [S/N]: ").strip().upper()

    if resp == "N":
        f = False