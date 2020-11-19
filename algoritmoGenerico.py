from random import choice, randint
from sanitiza import sanitiza_dados, preparacoes

# Inicializando as váriaveis de uso global.
dados = sanitiza_dados()
_tamanho_populacao = 0
_taxa_mutacao = 0
_taxa_cruzamento = 0
_max_geracoes = 0
_populacao, _individuo = [], []
_avaliacao = []
_escolhidos = []

# Iniciando as variáveis.
def inicia(tamanho_populacao, taxa_mutacao, taxa_cruzamento, max_geracoes):
    global _tamanho_populacao, _taxa_mutacao, _taxa_cruzamento, _max_geracoes

    _tamanho_populacao = tamanho_populacao
    _taxa_mutacao = taxa_mutacao
    _taxa_cruzamento = taxa_cruzamento
    _max_geracoes = max_geracoes

# Gerando a população inicial
def gerar_populacao():
    global _individuo

    # Inicializando uma população com o _tamanho_populacao.
    _populacao = [[] for i in range(_tamanho_populacao)]

    # Gerando as refeições aleatoriamente.
    for p in _populacao:
        refeicoes = [
            [choice([d for i, d in enumerate(dados[p])]) for p in preparacoes] for i in range(_tamanho_populacao)]
        _individuo.append(refeicoes)

    return _individuo[0]

# Minimizar o erro nutricional carb - 65, prot - 12,5 e lip - 10.
def _calcula_erro_nutricional(refeicao):
    carboidratos = 0
    proteinas = 0
    lipidios = 0

    p = preparacoes
    tipo = len(preparacoes) - 1
    contador = 0

    # Somando os valores totais de carboidratos, proteinas e lipidios totais da refeição.
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

# Avalia os individuos da população.
def avaliar(populacao_inicial):
    global _avaliacao

    for p in populacao_inicial:
        _avaliacao.append(_calcula_erro_nutricional(p))

# Busca os individuos com as melhores avaliações dentro da população.
def encontra_individuo_mais_apto(populacao_inicial):
    # Como são duas refeições prescisamos de dois inidivíduos mínimos diferentes.
    populacao_inicial = _encontra_valores_minimos(populacao_inicial)
    populacao_inicial = _encontra_valores_minimos(populacao_inicial)

    return _escolhidos

# Verifica se os valores de carb, lip e proteinas atuais são os menores.
def _verifica_menor_valor_nutricional(carboidratos, lipidios, proteinas, c):
    menor_carb = c[1]['Total_Carb'] < carboidratos
    menor_prot = c[1]['Total_Prot'] < proteinas
    menor_lip = c[1]['Total_Lip'] < lipidios

    return menor_carb and menor_prot and menor_lip

# Retorna o individuo com menor avaliação nutricional da população.
def _encontra_valores_minimos(populacao_inicial):
    global _escolhidos

    escolhido = []
    carboidratos, proteinas = 1000000000, 1000000000
    lipidios = carboidratos

    # Junta os arrays de população_inicial e avaliacao.
    candidatos = zip(populacao_inicial, _avaliacao)

    # Verificando se o candidato atual(c) tem os menores valores.
    for c in candidatos:
        if _verifica_menor_valor_nutricional(carboidratos, lipidios, proteinas, c):
            if not _escolhidos:
                escolhido = c
                carboidratos = c[1]['Total_Carb']
                proteinas = c[1]['Total_Prot']
                lipidios = c[1]['Total_Lip']
            elif _escolhidos[0] != c:
                escolhido = c
                carboidratos = c[1]['Total_Carb']
                proteinas = c[1]['Total_Prot']
                lipidios = c[1]['Total_Lip']

    _escolhidos.append(escolhido)
    # Deleta o escolhido da população inicial.
    del populacao_inicial[populacao_inicial.index(escolhido[0])]

    return populacao_inicial

def seleciona(populacao_inicial):
    # Junta os arrays de população_inicial e avaliacao.
    candidatos = zip(populacao_inicial, _avaliacao)

    individuo_1 = candidatos[randint(0, _tamanho_populacao - 1)]
    individuo_2 = candidatos[randint(0, _tamanho_populacao - 1)]

    comparacao_carb = individuo_1[1]['Total_Carb'] < individuo_1[2]['Total_Carb'] 
    comparacao_prot = individuo_1[1]['Total_Prot'] < individuo_1[2]['Total_Prot']
    comparacao_lip = individuo_1[1]['Total_Lip'] < individuo_1[2]['Total_Lip'] 

    if (comparacao_carb and comparacao_prot) or (comparacao_carb and comparacao_lip) or \
        (comparacao_lip and comparacao_prot):
        return individuo_1

    return individuo_2
