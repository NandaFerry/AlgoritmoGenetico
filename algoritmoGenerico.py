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
        self.populacao = [
            [choice([i for i, d in enumerate(dados[p])]) for p in preparacoes] for i in range(self.tamanho_populacao)]

        for individuo in self.populacao:
            for i in individuo:
                numero = float(i)
                individuo_binario = self._converte_float_binario(numero)

                for binario in individuo_binario:
                    individuo.append(binario)

        for i in individuo:
            print(i)

    def _converte_float_binario(self, numero):
        binario = format(unpack('!I', pack('!f', numero))[0], '032b')
        binario_sinal = f'+{binario}' if numero > 0 else f'-{binario}'

        return binario_sinal

    def descrever(self):
        saida = ''


a = AlgoritmoGenetico(1, 1, 1, 1)