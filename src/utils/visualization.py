import os
import numpy as np
import matplotlib.pyplot as plt

# def plot_tsp_solution(route, solution_label):
#     """
#     Plots the TSP solution and saves it to the figures folder inside src.
    
#     Arguments:
#     route : list - The order of city indices in the optimal path.
#     solution_label : str - Label for the solution (e.g., ACO or GA).
#     """
#     # Get the absolute path of the project directory
#     script_dir = os.path.dirname(os.path.abspath(__file__))  # utils/
#     src_dir = os.path.dirname(script_dir)  # src/
#     figures_dir = os.path.join(src_dir, 'figures')  # src/figures/

#     # Ensuring the path exists
#     os.makedirs(figures_dir, exist_ok=True)  

#     # Create the plot
#     plt.figure(figsize=(10, 6))
    
#     # Plot cities as points
#     x_coords = np.arange(len(route))
#     y_coords = np.zeros(len(route))
#     plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
    
#     plt.title(f"TSP Solution - {solution_label}")
#     plt.xlabel("City Index")
#     plt.ylabel("Y Coordinate")
#     plt.grid(True)

#     # Label the cities
#     for i, city in enumerate(route):
#         plt.text(i, 0.1, str(city), fontsize=9)

#     # Label the cities
#     for i, city in enumerate(route):
#         plt.text(i, 0.1, str(city), fontsize=9)

#     # Save the figure in the correct path
#     filename = f"tsp_solution_{solution_label.replace(' ', '_')}.png"
#     filepath = os.path.join(figures_dir, filename)
#     plt.savefig(filepath, dpi=300, bbox_inches='tight')

#     print(f"Plot saved: {filepath}")

#     # Show the plot
#     plt.show()


# def visualize_solution(aco_solution, ga_solution):
#     """
#     Visualizes TSP solutions from ACO and GA algorithms.
    
#     Arguments:
#     aco_solution : list - Best route returned by the ACO algorithm.
#     ga_solution : list - Best route returned by the GA algorithm.
#     """
#     print("Visualizing ACO Solution:")
#     plot_tsp_solution(aco_solution, "ACO Solution")

#     print("Visualizing GA Solution:")
#     plot_tsp_solution(ga_solution, "GA Solution")

RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../results"))
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
LOG_DIR = os.path.join(RESULTS_DIR, "log")
TABLES_DIR = os.path.join(RESULTS_DIR, "tables")

os.makedirs(FIGURES_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(TABLES_DIR, exist_ok=True)

def plot_tsp_solution(cities, path, filename="tsp_solution.png"):
    """Plots the TSP path and saves it."""
    plt.figure(figsize=(8, 6))
    cities = np.array(cities)
    
    for i in range(len(path) - 1):
        plt.plot([cities[path[i], 0], cities[path[i + 1], 0]], 
                 [cities[path[i], 1], cities[path[i + 1], 1]], "bo-")

    # Connect the last city back to the first
    plt.plot([cities[path[-1], 0], cities[path[0], 0]], 
             [cities[path[-1], 1], cities[path[0], 1]], "ro-")

    plt.scatter(cities[:, 0], cities[:, 1], c="red", marker="o")  # Mark cities
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("TSP Solution")

    file_path = os.path.join(FIGURES_DIR, filename)
    plt.savefig(file_path)
    plt.close()
    print(f"Saved TSP solution plot to {file_path}")

def save_log(data, filename="tsp_log.txt"):
    """Saves log information (e.g., best path and cost)."""
    file_path = os.path.join(LOG_DIR, filename)
    with open(file_path, "w") as f:
        f.write(data)
    print(f"Saved log to {file_path}")

def save_results_table(results, filename="tsp_results.csv"):
    """Saves a results table to a CSV file."""
    import pandas as pd
    df = pd.DataFrame(results)
    file_path = os.path.join(TABLES_DIR, filename)
    df.to_csv(file_path, index=False)
    print(f"Saved results table to {file_path}")
