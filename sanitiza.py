import csv

preparacoes = ['Arroz', 'Feijão', 'Salada', 'Guarnição', 'Principal', 'Suco', 'Sobremesa', 'Fruta']

# O arquivo deve ser convertido em csv
def sanitiza_dados():
  dados = {
        preparacoes[0]: {},
        preparacoes[1]: {},
        preparacoes[2]: {},
        preparacoes[3]: {},
        preparacoes[4]: {},
        preparacoes[5]: {},
        preparacoes[6]: {},
        preparacoes[7]: {}}

  # Arroz, Feijão, Salada, Guarnição, Principal, Suco e Sobremesa
  with open('Entrada.csv', encoding="utf-8") as entrada:
    leitor = csv.reader(entrada, delimiter=',')
    count = 0
    for linha in leitor:
      if count != 0:
        informacoes =  {'Codigo': linha[0], 'Carb': linha[3], 'Lip': linha[4], 'Pro': linha[5] }
        dados[linha[2]][linha[1]] = informacoes
      count += 1

    return dados
