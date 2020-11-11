import random
from aplicacao import sanitiza_dados
from aplicacao import preparacoes

dados = sanitiza_dados()

class AlgoritmoGenetico():

    def __init__(self, num_populacao, taxa_mutacao, taxa_cruzamento, limite):
        self.num_populacao = num_populacao
        self.taxa_mutacao = taxa_mutacao
        self.taxa_cruzamento = taxa_cruzamento
        self.limite = limite
        self.populacoes = []

    def gerarPopulacao(self):
        self.populacoes = [[random.choice([i for i,d in enumerate(dados[p])]) for p in preparacoes] for i in range(self.num_populacao)]
        print(self.populacoes)

    def descrever(self):
        saida = ''
        

a = AlgoritmoGenetico(3, 1, 1, 1)
a.gerarPopulacao()
a.descrever()