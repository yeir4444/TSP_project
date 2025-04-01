import os
import numpy as np
import matplotlib.pyplot as plt


def plot_tsp_solution(route, solution_label):
    """
    Plots the TSP solution and saves it to the figures folder inside src.
    
    Arguments:
    route : list - The order of city indices in the optimal path.
    solution_label : str - Label for the solution (e.g., ACO or GA).
    """
    # Get the absolute path of the project directory
    script_dir = os.path.dirname(os.path.abspath(__file__))  # utils/
    src_dir = os.path.dirname(script_dir)  # src/
    figures_dir = os.path.join(src_dir, 'figures')  # src/figures/

    # Ensuring the path exists
    os.makedirs(figures_dir, exist_ok=True)  

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

    # Label the cities
    for i, city in enumerate(route):
        plt.text(i, 0.1, str(city), fontsize=9)

    # Save the figure in the correct path
    filename = f"tsp_solution_{solution_label.replace(' ', '_')}.png"
    filepath = os.path.join(figures_dir, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')

    print(f"Plot saved: {filepath}")

    # Show the plot
    plt.show()


def visualize_solution(aco_solution, ga_solution):
    """
    Visualizes TSP solutions from ACO and GA algorithms.
    
    Arguments:
    aco_solution : list - Best route returned by the ACO algorithm.
    ga_solution : list - Best route returned by the GA algorithm.
    """
    print("Visualizing ACO Solution:")
    plot_tsp_solution(aco_solution, "ACO Solution")

    print("Visualizing GA Solution:")
    plot_tsp_solution(ga_solution, "GA Solution")
