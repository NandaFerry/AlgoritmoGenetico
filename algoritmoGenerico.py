from random import choice
from sanitiza import sanitiza_dados, preparacoes

dados = sanitiza_dados()
_tamanho_populacao = 0
_taxa_mutacao = 0
_taxa_cruzamento = 0
_max_geracoes = 0
_populacao, _individuo = [], []
_avaliacao = []
_escolhidos = []

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

    """ Somando os valores totais de carboidratos, proteinas e lipidios
        totais da refeição.""" 
    for r in refeicao:
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

# Avalia os individuos da população
def avaliar(populacao_inicial):
    global _avaliacao

    for p in populacao_inicial:
        _avaliacao.append(_calcula_erro_nutricional(p))

# Busca os individuos com as melhores avaliações dentro da população
def encontra_individuo_mais_apto(populacao_inicial):
    global _escolhidos

    quantidade = 0
    index = 0
    escolhido = []

    candidatos = zip(populacao_inicial, _avaliacao)

    while quantidade < 2:
        carboidratos = 10000000000000
        proteinas = carboidratos
        lipidios = carboidratos

        for c in candidatos:
            menor_carb = c[1]['Total_Carb'] < carboidratos
            menor_prot = c[1]['Total_Prot'] < proteinas
            menor_lip = c[1]['Total_Lip'] < lipidios

            if menor_carb and menor_prot and menor_lip:
                if len(_escolhidos) == 0:
                    escolhido = c
                    carboidratos = c[1]['Total_Carb']
                    proteinas = c[1]['Total_Prot']
                    lipidios = c[1]['Total_Lip']
                elif _escolhidos[0] != c:
                    escolhido = c
                    carboidratos = c[1]['Total_Carb']
                    proteinas = c[1]['Total_Prot']
                    lipidios = c[1]['Total_Lip']
        quantidade += 1
        _escolhidos.append(escolhido)

    return _escolhidos