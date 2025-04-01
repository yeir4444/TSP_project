import numpy as np
import matplotlib.pyplot as plt
from algorithms.aco import AntColony
from algorithms.ga import GeneticAlgorithm


def plot_tsp_solution(route, distances, solution_label):
    """
    Plots the TSP solution using the given route and distances.
    
    Arguments:
    route : list - The order of city indices in the optimal path.
    distances : np.array - Matrix of distances between cities.
    solution_label : str - Label for the solution (e.g., ACO or GA).
    """
    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot cities as points
    x_coords = np.arange(len(route))
    y_coords = np.zeros(len(route))
    plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
    
    plt.title(f"TSP Solution - {solution_label}")
    plt.xlabel("City Index")
    plt.ylabel("Y Coordinate")
    plt.grid(True)

    # Label the cities
    for i, city in enumerate(route):
        plt.text(i, 0.1, str(city), fontsize=9)

    # Show the plot
    plt.show()


def visualize_solution(aco_solution, ga_solution, distances):
    """
    Visualizes TSP solutions from ACO and GA algorithms.
    
    Arguments:
    aco_solution : list - Best route returned by the ACO algorithm.
    ga_solution : list - Best route returned by the GA algorithm.
    distances : np.array - Matrix of distances between cities.
    """
    print("Visualizing ACO Solution:")
    plot_tsp_solution(aco_solution, distances, "ACO Solution")

    print("Visualizing GA Solution:")
    plot_tsp_solution(ga_solution, distances, "GA Solution")
