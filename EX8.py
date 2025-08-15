"""
Faça chamada à API restcountries, que retorna informações sobre países, extraia essas
informações para as manipular conforme orientações abaixo. Por exemplo, ao acessar
https://restcountries.com/v3.1/name/brazil, onde brazil é o país escolhido, é retornado
em JSON vários dados sobre o Brasil, em posse disso você deve exibir no programa
que criará:
• Nome do país (Brasil), linguagem(s) (“Portuguese”...), região (“Americas”), subregião
(“South America”) com a capital (“Brasilia”)
• Sigla da moeda (BRL), nome (“Brazilian real”) e símbolo da moeda (“R$”)
• Países que fazem fronteira com o Brasil: “ARG”, “BOL”, “COL”, “GUF”, “GUY” ...
Permita que o usuário insira o nome do país (ex: italy, zambia, japan, canada, germany) e
são retornados esses dados.
"""

import requests

f = True
while f == True:
    nome_pais = str(input("Digite o nome de um país em inglês (Exemplos: italy, zambia, japan, canada, germany): ")).lower()
    response = requests.get(f"https://restcountries.com/v3.1/name/{nome_pais}")

    if response.status_code == 200:
        print("Sucesso!")
        res_json = response.json()
        info = res_json[0]

        nome_do_pais = info['name']['common']
        linguagem = info['languages']
        regiao = info['region']
        sub_regiao = info['subregion']
        capital = info['capital']

        S_M = info['currencies']
        fronteiras = info['borders']

        print(f"Nome do país: {nome_do_pais}")
        print(f"Linguagem do país: {linguagem}")
        print(f"Região do país: {regiao}")
        print(f"Sub-região do país: {sub_regiao}")
        print(f"Capital do país: {capital}\n")
        print(f"Sigla, nome e símbolo da moeda do país: {S_M}")
        print(f"Países que fazem com o país digitado: {fronteiras}")

        resp = input("Quer digitar outro país? [S/N]: ")
        if resp == "N":
            f = False
    else:
        print("Tivemos um problema")
        resp = input("Deseja tentar novamente ou até mesmo digitar outro país? [S/N]: ").strip().upper()
        if resp == "N":
            f = False