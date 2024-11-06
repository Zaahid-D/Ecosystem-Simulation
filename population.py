import random

# Species list
species_list = ["lion", "zebra", "giraffe", "buffalo", "elephant"]

def initialize_population(initial_population_size):
    population = []
    for i in range(initial_population_size):
        species = random.choice(species_list)
        age = random.randint(1, 10)
        health_status = random.uniform(0.5, 1.0)
        offspring = []
        animal = {'species': species, 'age': age, 'health_status': health_status, 'offspring': offspring}
        population.append(animal)
    return population

def update_population(population, average_birth_rate, average_mortality_rate, average_migration_rate, depth=0):
    new_population = []
    for animal in population:
        animal['age'] += 1
        if random.random() < average_mortality_rate:
            continue
        if random.random() < average_migration_rate:
            continue
        if random.random() < average_birth_rate:
            new_animal = {'species': animal['species'], 'age': 1, 'health_status': random.uniform(0.5, 1), 'offspring': []}
            animal['offspring'].append(new_animal)
            new_population.append(new_animal)
            new_population += update_population([new_animal], average_birth_rate, average_mortality_rate, average_migration_rate, depth+1)
        new_population.append(animal)
    return new_population