import random

def genetic_algorithm(population, fitness, generations=100):
    for _ in range(generations):
        population = sorted(population, key=fitness)
        next_generation = population[:2]
        for _ in range(len(population) - 2):
            parent1, parent2 = random.sample(population[:10], 2)
            child = crossover(parent1, parent2)
            mutate(child)
            next_generation.append(child)
        population = next_generation
    return population[0]

def fitness(route):
    return sum(distances[route[i-1]][route[i]] for i in range(len(route)))

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = parent1[start:end]
    child += [city for city in parent2 if city not in child]
    return child

def mutate(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]

distances = {
    'A': {'B': 2, 'C': 9, 'D': 10},
    'B': {'A': 2, 'C': 6, 'D': 4},
    'C': {'A': 9, 'B': 6, 'D': 8},
    'D': {'A': 10, 'B': 4, 'C': 8}
}
population = [list(distances.keys()) for _ in range(10)]
for individual in population:
    random.shuffle(individual)
best_route = genetic_algorithm(population, fitness)
print("Best route:", best_route)


## =============================================================================

def genetic_algorithm(population, generations=1000):
    for _ in range(generations):
        population = sorted(population, key=fitness)
        population = population[:len(population) // 2]
        offspring = []
        for _ in range(len(population) // 2):
            parents = random.sample(population, 2)
            child = crossover(parents[0], parents[1])
            child = mutate(child)
            offspring.append(child)
        population.extend(offspring)
    return min(population, key=fitness)

def crossover(parent1, parent2):
    return parent1[:len(parent1) // 2] + parent2[len(parent2) // 2:]

def mutate(path, mutation_rate=0.1):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(path)), 2)
        path[i], path[j] = path[j], path[i]
    return path
