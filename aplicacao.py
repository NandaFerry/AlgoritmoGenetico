""" Algoritmo Genético para gerar um cardápio nutricional implementado por: 
Carolline Rodrigues, Fernanda Ferry, Vitória Maria e Yago Teixeira""" 
import csv

# O arquivo deve ser convertido em csv
def sanitiza_dados():
  dados = {
        'Arroz':{},
        'Feijão': {},
        'Salada': {},
        'Guarnição': {},
        'Principal': {},
        'Suco': {},
        'Sobremesa': {},
        'Fruta': {}}

  # Arroz, Feijão, Salada, Guarnição, Principal, Suco e Sobremesa
  with open('/content/Entrada.csv') as entrada:
    leitor = csv.reader(entrada, delimiter=',')
    count = 0
    for linha in leitor:
      if count != 0:
        informacoes =  {'Código': linha[0], 'Carb': linha[3], 'Lip': linha[4], 'Pro': linha[5] }
        dados[linha[2]][linha[1]] = informacoes
      count += 1

    return dados

sanitiza_dados()

def executa():
    pass