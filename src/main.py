from algorithms.aco import AntColony
from algorithms.ga import GeneticAlgorithm
from utils.tsp_utils import load_distance_matrix
from utils.tsp_utils import compute_tour_length
from utils.visualization import visualize_solution

# Load distance matrix
distances = load_distance_matrix("data/city_distances.csv")

# Run ACO
aco = AntColony(distances)
best_aco_path, best_aco_length = aco.run()
best_aco_tour_length = compute_tour_length(best_aco_path, distances)
print(f"ACO Best Path: {best_aco_path}, Distance: {best_aco_tour_length}")

# Run GA
ga = GeneticAlgorithm(distances)
best_ga_path, best_ga_length = ga.run()
best_ga_tour_length = compute_tour_length(best_ga_path, distances)
print(f"GA Best Path: {best_ga_path}, Distance: {best_ga_tour_length}")

# Visualize the solutions
visualize_solution(best_aco_path, best_ga_path, distances)
