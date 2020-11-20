""" Algoritmo Genético para gerar um cardápio nutricional implementado por:
Carolline Rodrigues, Fernanda Ferry, Vitória Maria, Jefferson e Yago Teixeira"""

from algoritmoGenerico import gerar_populacao, inicia, avaliar, encontra_individuo_mais_apto,\
    seleciona, crossover, mutacao

tamanho_populacao = 100
taxa_mutacao = 20
taxa_cruzamento = 45
max_geracoes = 3

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
    
    r = 1
    for individuo in individuos:
        # Imprimindo os resultados começando com a população inicial.
        print('Refeição {} Resultado {}: {}\n'.format(r, i, individuo))
        r += 1
        populacao.append(individuo)

    populacao.append(populacao_inicial)

    # Inicializando uma nova população.
    nova_populacao = []
    while len(nova_populacao) < tamanho_populacao:

        # Selecionando os 'pais'.
        pai, mae = seleciona(populacao)

        while mae == pai:
            pai, mae = seleciona(populacao)

        # Realizar o crossover dos pais e gerar os filhos.
        filho_1, filho_2 = crossover(pai, mae)
        
        # Realiza a mutação.
        filho_1 = mutacao(filho_1)
        filho_2 = mutacao(filho_2)

        nova_populacao.append(filho_1)
        nova_populacao.append(filho_2)
    
    # Substitui a população antiga pela nova e realiza sua avaliação.
    populacao_inicial = nova_populacao
    avaliar(populacao_inicial)

print('\n================================================================================\n')
individuos = encontra_individuo_mais_apto(populacao_inicial)
r = 1
for individuo in individuos:
    # Imprimindo os resultados começando com a população inicial.
    print('Refeição {} Resultado Final: {}\n'.format(r, individuo))
    r += 1
    if r == 3: 
        break