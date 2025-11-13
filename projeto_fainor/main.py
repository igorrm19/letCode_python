print("hello world")

import random

# ---------------- GERAÇÃO DA POPULAÇÃO INICIAL ----------------
# Conjunto de soluções possíveis para o problema da mochila.
# Cada indivíduo indica, com 0 e 1, quais itens estão ou não na mochila.

num_itens = 5
tamanho_populacao = 10
capacidade_mochila = 15

# Gerar valores e pesos aleatórios para os itens
valores = [random.randint(10, 100) for _ in range(num_itens)]
pesos = [random.randint(1, 10) for _ in range(num_itens)]

# Gerar população inicial (lista de listas binárias)
populacao = [
    [random.randint(0, 1) for _ in range(num_itens)]
    for _ in range(tamanho_populacao)
]

print("Valores dos Itens:", valores)
print("Pesos dos Itens:", pesos)
print("População Inicial:", populacao)


# ---------------- FUNÇÃO DE AVALIAÇÃO (FITNESS) ----------------
# A função de avaliação calcula o valor total dos itens na mochila.
# Caso o peso total ultrapasse a capacidade, o fitness é 0 (penalização).

def calcular_fitness(individuo, valores, pesos, capacidade):
    total_valor = 0
    total_peso = 0
    for i in range(len(individuo)):
        if individuo[i] == 1:
            total_valor += valores[i]
            total_peso += pesos[i]
    if total_peso > capacidade:
        return 0
    return total_valor


# ---------------- SELEÇÃO ----------------
# Seleciona os indivíduos mais aptos (maior fitness).
# Aqui usamos a seleção por torneio simples.

def selecao_torneio(populacao, fitness, tamanho_torneio=3):
    selecionados = []
    for _ in range(2):  # selecionar dois pais
        competidores = random.sample(list(zip(populacao, fitness)), tamanho_torneio)
        competidores.sort(key=lambda x: x[1], reverse=True)
        selecionados.append(competidores[0][0])
    return selecionados


# ---------------- CRUZAMENTO (CROSSOVER) ----------------
# Combina dois indivíduos pais para gerar filhos.
# Aqui usamos crossover de um ponto.

def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2


# ---------------- MUTAÇÃO ----------------
# Altera aleatoriamente bits de um indivíduo para manter diversidade.

def mutacao(individuo, taxa_mutacao=0.1):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  # inverte o bit
    return individuo


# ---------------- NOVA GERAÇÃO ----------------
# Cria novas gerações até encontrar uma solução satisfatória.

geracoes = 10

for geracao in range(geracoes):
    # Avaliar a população
    fitness = [calcular_fitness(ind, valores, pesos, capacidade_mochila) for ind in populacao]
    print(f"Geração {geracao + 1} - Fitness: {fitness}")

    # Nova população
    nova_populacao = []

    # Gerar filhos até preencher nova população
    while len(nova_populacao) < tamanho_populacao:
        pais = selecao_torneio(populacao, fitness)
        filhos = crossover(pais[0], pais[1])
        nova_populacao.extend([mutacao(filhos[0]), mutacao(filhos[1])])

    # Atualizar população
    populacao = nova_populacao[:tamanho_populacao]

# Avaliar população final
fitness_final = [calcular_fitness(ind, valores, pesos, capacidade_mochila) for ind in populacao]
melhor_indice = fitness_final.index(max(fitness_final))
melhor_solucao = populacao[melhor_indice]

print("\nMelhor solução encontrada:", melhor_solucao)
print("Valor total:", max(fitness_final))
print("Peso total:", sum([pesos[i] for i in range(num_itens) if melhor_solucao[i] == 1]))
