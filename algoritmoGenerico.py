from random import choice
from sanitiza import sanitiza_dados, preparacoes

dados = sanitiza_dados()
_tamanho_populacao = 0
_taxa_mutacao = 0
_taxa_cruzamento = 0
_max_geracoes = 0
_populacao = []
_individuo = []
_avaliacao = []

# Iniciando as variáveis
def inicia(tamanho_populacao, taxa_mutacao, taxa_cruzamento, max_geracoes):
    global _tamanho_populacao, _taxa_mutacao, _taxa_cruzamento, _max_geracoes
    
    _tamanho_populacao = tamanho_populacao
    _taxa_mutacao = taxa_mutacao
    _taxa_cruzamento = taxa_cruzamento
    _max_geracoes = max_geracoes

# Gerando a população inicial
def gerar_populacao():
    global _individuo

    # Inicializando uma população com o _tamanho_populacao
    _populacao = [[] for i in range(_tamanho_populacao)]

    # Gerando as refeições aleatoriamente
    for p in _populacao:
        refeicoes = [
            [choice([d for i, d in enumerate(dados[p])]) for p in preparacoes] for i in range(_tamanho_populacao)]
        _individuo.append(refeicoes)
    
    return _individuo[0]

# Minimizar o erro nutricional carb - 65, prot - 12,5 e lip - 10
def _calcula_erro_nutricional(refeicao):
    carboidratos = 0
    proteinas = 0
    lipidios = 0

    p = preparacoes
    tipo = len(preparacoes) - 1
    contador = 0

    for r in refeicao[0]:
        if contador > tipo:
            break
        carboidratos += float(dados[p[contador]][r]['Carb'])
        proteinas += float(dados[p[contador]][r]['Pro'])
        lipidios += float(dados[p[contador]][r]['Lip'])

        contador += 1

    avaliacao = {
        'Total_Carb': round(carboidratos - 65, 2), 
        'Total_Prot': round(proteinas - 12.5, 2),
        'Total_Lip': round(lipidios - 10, 2)
        }

    return avaliacao

def avaliar(populacao_inicial):
    global _avaliacao

    for p in populacao_inicial:
        _avaliacao.append(_calcula_erro_nutricional(p))
    
