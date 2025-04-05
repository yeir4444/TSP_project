import numpy as np
import pandas as pd
import random

class GeneticAlgorithm:
    def __init__(self, distances, population_size=100, generations=500, mutation_rate=0.02):
        """
        {
            "description": "Initializes the Genetic Algorithm for solving the TSP.",
            "parameters": {
                "distances": "2D numpy array representing distances between cities.",
                "population_size": "Number of candidate solutions (individuals) in each generation.",
                "generations": "Number of generations to evolve the population.",
                "mutation_rate": "Probability of mutating a solution."
            },
            "returns": "None"
        }
        """
        self.distances = distances
        self.n_cities = distances.shape[0]
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def run(self):
        """
        {
            "description": "Executes the Genetic Algorithm to find a near-optimal solution for the TSP.",
            "parameters": {},
            "returns": {
                "best_solution": "List of city indices representing the best path found.",
                "best_length": "Total distance of the best path."
            }
        }
        """
        population = [self._random_solution() for _ in range(self.population_size)]
        for _ in range(self.generations):
            fitness_scores = [self._evaluate(solution) for solution in population]
            population = self._next_generation(population, fitness_scores)
        best_solution = min(population, key=self._evaluate)
        return best_solution, self._evaluate(best_solution)

    def _random_solution(self):
        """
        {
            "description": "Generates a random tour by shuffling city indices.",
            "parameters": {},
            "returns": {
                "solution": "List of city indices representing a random tour."
            }
        }
        """
        solution = list(range(self.n_cities))
        random.shuffle(solution)
        return solution

    def _evaluate(self, solution):
        """
        {
            "description": "Calculates the total distance of a given TSP path.",
            "parameters": {
                "solution": "List of city indices representing a tour."
            },
            "returns": {
                "total_distance": "Total distance of the tour including return to the start."
            }
        }
        """
        return sum(self.distances[solution[i], solution[i+1]] for i in range(len(solution)-1)) + self.distances[solution[-1], solution[0]]

    def _next_generation(self, population, fitness_scores):
        """
        {
            "description": "Generates the next generation of the population using selection, crossover, and mutation.",
            "parameters": {
                "population": "List of current solutions (paths).",
                "fitness_scores": "List of distances (lower is better) for each solution."
            },
            "returns": {
                "new_population": "List of evolved solutions for the next generation."
            }
        }
        """
        new_population = [self._crossover(*self._select_parents(population, fitness_scores)) for _ in range(self.population_size)]
        return [self._mutate(child) for child in new_population]

    def _select_parents(self, population, fitness_scores):
        """
        {
            "description": "Selects two parents for crossover using tournament selection.",
            "parameters": {
                "population": "List of current solutions.",
                "fitness_scores": "List of corresponding distances for each solution."
            },
            "returns": {
                "parent1": "First parent selected for crossover.",
                "parent2": "Second parent selected for crossover."
            },
            "notes": "Both parents are the best individual from a random subset of the population (tournament of size 5)."
        }
        """
        tournament = random.sample(list(zip(population, fitness_scores)), k=5)
        return min(tournament, key=lambda x: x[1])[0], min(tournament, key=lambda x: x[1])[0]

    def _crossover(self, parent1, parent2):
        """
        {
            "description": "Creates a child solution by combining segments of two parent solutions using ordered crossover (OX).",
            "parameters": {
                "parent1": "First parent path.",
                "parent2": "Second parent path."
            },
            "returns": {
                "child": "New solution combining genetic material from both parents."
            }
        }
        """
        start, end = sorted(random.sample(range(self.n_cities), 2))
        child = [None] * self.n_cities
        child[start:end] = parent1[start:end]
        fill_values = [city for city in parent2 if city not in child]
        child = [city if city is not None else fill_values.pop(0) for city in child]
        return child

    def _mutate(self, solution):
        """
        {
            "description": "Randomly swaps two cities in the tour with a certain mutation probability.",
            "parameters": {
                "solution": "List of city indices representing the tour."
            },
            "returns": {
                "mutated_solution": "Mutated version of the original solution (may be unchanged)."
            }
        }
        """
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(solution)), 2)
            solution[i], solution[j] = solution[j], solution[i]
        return solution

# distances = pd.read_csv("data/city_distances.csv").to_numpy()
# ga = GeneticAlgorithm(distances)
# best_path, best_length = ga.run()
# print("Best Path:", best_path, "Best Distance:", best_length)
