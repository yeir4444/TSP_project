import numpy as np
import pandas as pd
import random

class GeneticAlgorithm:
    def __init__(self, distances, population_size=100, generations=500, mutation_rate=0.02):
        self.distances = distances
        self.n_cities = distances.shape[0]
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def run(self):
        population = [self._random_solution() for _ in range(self.population_size)]
        for _ in range(self.generations):
            fitness_scores = [self._evaluate(solution) for solution in population]
            population = self._next_generation(population, fitness_scores)
        best_solution = min(population, key=self._evaluate)
        return best_solution, self._evaluate(best_solution)

    def _random_solution(self):
        solution = list(range(self.n_cities))
        random.shuffle(solution)
        return solution

    def _evaluate(self, solution):
        return sum(self.distances[solution[i], solution[i+1]] for i in range(len(solution)-1)) + self.distances[solution[-1], solution[0]]

    def _next_generation(self, population, fitness_scores):
        new_population = [self._crossover(*self._select_parents(population, fitness_scores)) for _ in range(self.population_size)]
        return [self._mutate(child) for child in new_population]

    def _select_parents(self, population, fitness_scores):
        tournament = random.sample(list(zip(population, fitness_scores)), k=5)
        return min(tournament, key=lambda x: x[1])[0], min(tournament, key=lambda x: x[1])[0]

    def _crossover(self, parent1, parent2):
        start, end = sorted(random.sample(range(self.n_cities), 2))
        child = [None] * self.n_cities
        child[start:end] = parent1[start:end]
        fill_values = [city for city in parent2 if city not in child]
        child = [city if city is not None else fill_values.pop(0) for city in child]
        return child

    def _mutate(self, solution):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(solution)), 2)
            solution[i], solution[j] = solution[j], solution[i]
        return solution

# distances = pd.read_csv("data/city_distances.csv").to_numpy()
# ga = GeneticAlgorithm(distances)
# best_path, best_length = ga.run()
# print("Best Path:", best_path, "Best Distance:", best_length)
