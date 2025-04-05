import numpy as np
import pandas as pd

class AntColony:
    def __init__(self, distances, n_ants=10, n_iterations=100, alpha=1, beta=2, evaporation=0.5, pheromone_init=1.0):
        """
        {
            "description": "Initializes the Ant Colony Optimization (ACO) algorithm with the given parameters.",
            "parameters": {
                "distances": "2D numpy array representing distances between cities.",
                "n_ants": "Number of ants to simulate in each iteration.",
                "n_iterations": "Number of iterations to run the algorithm.",
                "alpha": "Influence of pheromone concentration on path selection.",
                "beta": "Influence of heuristic desirability (visibility) on path selection.",
                "evaporation": "Pheromone evaporation rate after each iteration.",
                "pheromone_init": "Initial pheromone value on all paths."
            },
            "returns": "None"
        }
        """
        self.distances = distances
        self.n_cities = distances.shape[0]
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation
        self.pheromones = np.ones((self.n_cities, self.n_cities)) * pheromone_init

    
    def run(self):
        """
        {
            "description": "Executes the ACO algorithm to find the shortest tour.",
            "parameters": {},
            "returns": {
                "best_path": "List of city indices representing the best tour found.",
                "best_length": "Total distance of the best tour."
            }
        }
        """
        best_path = None
        best_length = float('inf')

        for _ in range(self.n_iterations):
            paths, lengths = self._construct_solutions()
            self._update_pheromones(paths, lengths)

            min_length = min(lengths)
            if min_length < best_length:
                best_length = min_length
                best_path = paths[np.argmin(lengths)]

        return best_path, best_length

    
    def _construct_solutions(self):
        """
        {
            "description": "Generates complete paths for all ants and evaluates their lengths.",
            "parameters": {},
            "returns": {
                "paths": "List of paths, each a list of city indices.",
                "lengths": "List of distances corresponding to each path."
            }
        }
        """
        paths = []
        lengths = []
        for _ in range(self.n_ants):
            path = self._generate_path()
            length = self._calculate_path_length(path)
            paths.append(path)
            lengths.append(length)
        return paths, lengths

    
    def _generate_path(self):
        """
        {
            "description": "Generates a single valid path for an ant using probabilistic selection.",
            "parameters": {},
            "returns": {
                "path": "List of city indices forming a complete tour."
            }
        }
        """
        path = [np.random.randint(self.n_cities)]
        while len(path) < self.n_cities:
            next_city = self._select_next_city(path[-1], path)
            path.append(next_city)
        return path

    
    def _select_next_city(self, current_city, visited):
        """
        {
            "description": "Selects the next city for an ant based on transition probabilities.",
            "parameters": {
                "current_city": "Index of the current city.",
                "visited": "List of already visited cities."
            },
            "returns": {
                "next_city": "Index of the next selected city."
            }
        }
        """
        probabilities = self._calculate_transition_probabilities(current_city, visited)
        return np.random.choice(range(self.n_cities), p=probabilities)

    
    def _calculate_transition_probabilities(self, current_city, visited):
        """
        {
            "description": "Calculates the probability distribution over the next possible cities.",
            "parameters": {
                "current_city": "Index of the current city.",
                "visited": "List of visited city indices to avoid."
            },
            "returns": {
                "probabilities": "Normalized numpy array representing transition probabilities to each city."
            },
            "notes": "Uses both pheromone levels and inverse distances (visibility) to compute probabilities."
        }
        """
        pheromone = self.pheromones[current_city]
        visibility = 1 / (self.distances[current_city] + 1e-10)
        probabilities = (pheromone ** self.alpha) * (visibility ** self.beta)
        probabilities[visited] = 0
        return probabilities / probabilities.sum()

    
    def _calculate_path_length(self, path):
        """
        {
            "description": "Calculates the total distance of a complete TSP path, including return to the start city.",
            "parameters": {
                "path": "List of city indices representing the tour."
            },
            "returns": {
                "length": "Total distance of the path including the closing leg."
            }
        }
        """
        return sum(self.distances[path[i], path[i+1]] for i in range(len(path)-1)) + self.distances[path[-1], path[0]]

    
    def _update_pheromones(self, paths, lengths):
        """
        {
            "description": "Calculates the total distance of a complete TSP path, including return to the start city.",
            "parameters": {
                "path": "List of city indices representing the tour."
            },
            "returns": {
                "length": "Total distance of the path including the closing leg."
            }
        }
        """
        self.pheromones *= (1 - self.evaporation)
        for path, length in zip(paths, lengths):
            for i in range(len(path)-1):
                self.pheromones[path[i], path[i+1]] += 1 / length


# distances = pd.read_csv("data/city_distances.csv").to_numpy()
# aco = AntColony(distances)
# best_path, best_length = aco.run()
# print("Best Path:", best_path, "Best Distance:", best_length)
