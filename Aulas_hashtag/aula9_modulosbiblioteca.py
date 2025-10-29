#import os

#print(os.getcwd())
#lista_arquivos = os.listdir("Aulas_Hashtag")
#print(lista_arquivos)


import requests
caminho = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

retorno = requests.get(caminho)
print(retorno)
print(retorno.json()) #A resposta em Json é um dicionário python

dic_respost = retorno.json()

for moeda in dic_respost:
    dic_moeda = dic_respost[moeda]["bid"]
    print(moeda, dic_moeda)
