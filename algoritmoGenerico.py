from random import choice
from sanitiza import sanitiza_dados, preparacoes
from struct import unpack, pack

dados = sanitiza_dados()

class AlgoritmoGenetico():

    def __init__(self, tamanho_populacao, taxa_mutacao, taxa_cruzamento, limite):
        self.tamanho_populacao = tamanho_populacao
        self.taxa_mutacao = taxa_mutacao
        self.taxa_cruzamento = taxa_cruzamento
        self.limite = limite
        self.populacao = []

        self._gerarPopulacao()

    def _gerarPopulacao(self):
        self.populacao = [[] for i in range(self.tamanho_populacao)]

        for individuo in self.populacao:
            refeicoes = [[choice([d for i, d in enumerate(dados[p])]) for p in preparacoes] for i in range(self.tamanho_populacao)]
            individuo.append(refeicoes)

        for f in individuo:
            print(f)

    def _converte_float_binario(self, numero):
        binario = format(unpack('!I', pack('!f', numero))[0], '032b')
        if numero > 0:
            binario_sinal = f'+{str(binario)}'
        else:
            binario_sinal = f'-{str(binario)}'

        return binario_sinal

    def descrever(self):
        saida = ''


a = AlgoritmoGenetico(2, 1, 1, 1)
