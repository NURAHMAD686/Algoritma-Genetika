import time
import random
import string

start_time = time.time()
target = 'PEMROGRAMAN LANJUTAN'
population_size =50
mutation_rate = 0.05
generations = 50000
# Function to initialize population
def initialize_population(size, length):
    population = [''.join(random.choices(string.ascii_letters + " ,!", k=length)) for _ in range(size)]
    return population

# Function to calculate fitness of an individual
def calculate_fitness(individual):
    return sum(1 for i, c in enumerate(individual) if c == target[i])

# Function to select individuals based on fitness
def selection(population):
    weights = [calculate_fitness(ind) for ind in population]
    total_fitness = sum(weights)
    if total_fitness == 0:
        probabilities = [1 / len(weights) for _ in weights]
    else:
        probabilities = [w / total_fitness for w in weights]
    selected = random.choices(population, probabilities, k=2)
    return selected

# Function to perform crossover with two parents
def crossover_two_parents(parent1, parent2):
    len_individual = len(parent1)
    crossover_point1 = random.randint(1, len_individual - 1)
    crossover_point2 = random.randint(crossover_point1, len_individual)
    
    child1 = parent1[:crossover_point1] + parent2[crossover_point1:crossover_point2] + parent1[crossover_point2:] 
    child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:] 
    # child2 = parent2[crossover_point2:] + parent1[crossover_point1:crossover_point2] + parent2[:crossover_point1] 
    # child2 = parent2[:crossover_point1] + parent1[crossover_point1:crossover_point2] + parent2[crossover_point2:] 
    return child1, child2

# Function to perform mutation
def mutate(individual, mutation_rate):
    return ''.join(
        char if random.random() > mutation_rate else random.choice(string.ascii_letters + " ,!")
        for char in individual
    )

# Main genetic algorithm function
def genetic_algorithm():
    population = initialize_population(population_size, len(target))
    for generation in range(generations): 
        population = sorted(population, key=calculate_fitness, reverse=True)
        if calculate_fitness(population[0]) == len(target):
            break
        next_population = population[:10]  # Elitism: retain top individuals
        while len(next_population) < population_size:
            parent1, parent2, parent3 = random.sample(population[:10], 3)  # Top 10 for better chances
            child1, child2 = crossover_two_parents(parent1, parent2)
            next_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
        population = next_population[:population_size]
        print(f"G eneration {generation + 1}: Best fitness = {calculate_fitness(population[0])}, Best individual = {population[0]}")
    return population[0]

best_individual = genetic_algorithm()
print(f"Best individual after {generations} generations: {best_individual}")

waktu = time.time() - start_time
print('\nWaktu komputasi: ', waktu, 'detik\n')
print('kecepatan running: ', round((generations+1)/waktu), 'generasi/detik\n')