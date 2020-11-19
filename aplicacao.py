""" Algoritmo Genético para gerar um cardápio nutricional implementado por:
Carolline Rodrigues, Fernanda Ferry, Vitória Maria, Jefferson e Yago Teixeira"""

from algoritmoGenerico import gerar_populacao, inicia, avaliar, encontra_individuo_mais_apto, seleciona

tamanho_populacao = 3 # Tamanho da população inicial
taxa_mutacao = 1 # Taxa de mutação
taxa_cruzamento = 1 # Taxa de cruzamento
max_geracoes = 1 # Máximo de vezes que serão geradas as populações

# Iniciando as variáveis
inicia(tamanho_populacao, taxa_mutacao, taxa_cruzamento, max_geracoes)

# Gerando a população inicial
populacao_inicial = gerar_populacao()

# Avalia a população inicial
avaliar(populacao_inicial)

populacao_total = populacao_inicial 

for i in range(max_geracoes):
    # Encontra o individuo com a menor avaliação
    individuos = encontra_individuo_mais_apto(populacao_inicial)

    for individuo in individuos:
        # Imprimindo os resultados começando com a população inicial
        print('Resultado {}: {}\n'.format(i, individuo))

        # Inicializando uma nova população
        nova_populacao = []

    while len(nova_populacao) < tamanho_populacao:

        # Selecionando os 'pais'.
        pai = seleciona(populacao_total)
        mae = seleciona(populacao_total)