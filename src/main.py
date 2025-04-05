import numpy as np
from algorthims.aco import AntColony 
from algorthims.ga import GeneticAlgorithm 
from utils.tsp_utils import load_distance_matrix
from utils.tsp_utils import compute_tour_length
from utils.visualization import plot_tsp_solution, save_log, save_results_table


def main():
    """
    {
        "name": "main",
        "description": "Runs the main execution flow for solving the TSP using Ant Colony Optimization (ACO) and Genetic Algorithm (GA). Loads data, runs both algorithms, saves plots, logs, and a comparison table.",
        "parameters": None,
        "returns": null,
        "steps": [
            "Load distance matrix from CSV file",
            "Generate random city coordinates for visualization",
            "Run the ACO algorithm and retrieve the best path and distance",
            "Save the ACO path log and plot the ACO solution",
            "Run the GA algorithm and retrieve the best path and distance",
            "Save the GA path log and plot the GA solution",
            "Save the comparison of both algorithm results in a CSV table",
            "Print success messages"
        ],
        "notes": [
            "City coordinates are generated randomly and used only for visualization.",
            "Actual tour distance is computed from the distance matrix, not coordinates.",
            "Results are saved in the results/ directory relative to the root."
        ]
    }
    """
    # Load distance matrix
    distances = load_distance_matrix("../data/city_distances.csv")
    
    # Generate random city coordinates for visualization (Replace this with actual coordinates if available)
    num_cities = distances.shape[0]
    city_coords = np.random.rand(num_cities, 2) * 100  # 100x100 grid for visualization
    
    # Run ACO
    aco = AntColony(distances)
    best_aco_path, best_aco_length = aco.run()
    best_aco_tour_length = compute_tour_length(best_aco_path, distances)
    print(f"ACO Best Path: {best_aco_path}, Distance: {best_aco_tour_length}")
    
    # Save ACO results
    save_log(f"ACO Best Path: {best_aco_path}\nACO Best Distance: {best_aco_length}", "aco_log.txt")
    plot_tsp_solution(city_coords, best_aco_path, "aco_solution.png")
    
    
    # Run GA
    ga = GeneticAlgorithm(distances)
    best_ga_path, best_ga_length = ga.run()
    best_ga_tour_length = compute_tour_length(best_ga_path, distances)
    print(f"GA Best Path: {best_ga_path}, Distance: {best_ga_tour_length}")
    
    # Save GA results
    save_log(f"GA Best Path: {best_ga_path}\nGA Best Distance: {best_ga_length}", "ga_log.txt")
    plot_tsp_solution(city_coords, best_ga_path, "ga_solution.png")
    
    # Save comparison results in a table
    results_data = [
        {"Algorithm": "ACO", "Best Distance": best_aco_length},
        {"Algorithm": "GA", "Best Distance": best_ga_length},
    ]
    save_results_table(results_data, "tsp_comparison.csv")
    
    print("All results saved successfully!")
    # Visualize the solutions
    # visualize_solution(best_aco_path, best_ga_path)
    

if __name__ == '__main__':
    main() 
