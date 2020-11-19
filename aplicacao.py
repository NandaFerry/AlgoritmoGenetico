""" Algoritmo Genético para gerar um cardápio nutricional implementado por: 
Carolline Rodrigues, Fernanda Ferry, Vitória Maria, Jefferson e Yago Teixeira""" 

from algoritmoGenerico import gerar_populacao, inicia, calcula_erro_nutricional

tamanho_populacao = 1 # Tamanho da população inicial
taxa_mutacao = 1 # Taxa de mutação
taxa_cruzamento = 1 # Taxa de cruzamento
max_geracoes = 2 # Máximo de vezes que serão geradas as populações

# Iniciando as variáveis
inicia(tamanho_populacao, taxa_mutacao, taxa_cruzamento, max_geracoes)

# Gerando a população inicial
populacao_inicial = gerar_populacao()

print(calcula_erro_nutricional(populacao_inicial))

