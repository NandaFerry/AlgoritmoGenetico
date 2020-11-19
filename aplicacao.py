""" Algoritmo Genético para gerar um cardápio nutricional implementado por:
Carolline Rodrigues, Fernanda Ferry, Vitória Maria, Jefferson e Yago Teixeira"""

from algoritmoGenerico import gerar_populacao, inicia, avaliar, encontra_individuo_mais_apto, seleciona, crossover

tamanho_populacao = 5
taxa_mutacao = 1
taxa_cruzamento = 1
max_geracoes = 1

# Iniciando as variáveis.
inicia(tamanho_populacao, taxa_mutacao, taxa_cruzamento, max_geracoes)

# Gerando a população inicial.
populacao_inicial = gerar_populacao()

# Avalia a população inicial.
avaliar(populacao_inicial)
populacao = []

for i in range(max_geracoes):
    # Encontra o individuo com a menor avaliação.
    individuos = encontra_individuo_mais_apto(populacao_inicial)

    for individuo in individuos:
        # Imprimindo os resultados começando com a população inicial.
        print('Resultado {}: {}\n'.format(i, individuo))
        populacao.append(individuo)

    populacao.append(populacao_inicial)

    # Inicializando uma nova população.
    nova_populacao = []
    while len(nova_populacao) < tamanho_populacao:

        # Selecionando os 'pais'.
        pai = seleciona(populacao)
        mae = seleciona(populacao)

        # Realizar o crossover dos pais e gerar os filhos.
        filho_1, filho_2 = crossover(pai, mae)

        print(filho_1)
        print(filho_2)

        break