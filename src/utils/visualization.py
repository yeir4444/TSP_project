import os
import numpy as np
import matplotlib.pyplot as plt


RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../results"))
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
LOG_DIR = os.path.join(RESULTS_DIR, "log")
TABLES_DIR = os.path.join(RESULTS_DIR, "tables")

os.makedirs(FIGURES_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(TABLES_DIR, exist_ok=True)

def plot_tsp_solution(cities, path, filename="tsp_solution.png"):
    """
    {
        "summary": "Plots the TSP path using city coordinates and saves the figure.",
        "parameters": {
            "cities": "list or np.ndarray - A list/array of (x, y) city coordinates.",
            "path": "list - The order of city indices in the TSP solution.",
            "filename": "str - The name of the file to save the plot to (default is 'tsp_solution.png')."
        },
        "output": "A PNG image is saved in the 'figures' directory.",
        "prints": "The full file path where the plot is saved."
    }
    """
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
    """
    {
        "summary": "Saves textual log data (e.g., best path, fitness) to a file.",
        "parameters": {
            "data": "str - The log information to save.",
            "filename": "str - The name of the file to save the log to (default is 'tsp_log.txt')."
        },
        "output": "A .txt file is saved in the 'log' directory.",
        "prints": "The full file path where the log is saved."
    }
    """
    file_path = os.path.join(LOG_DIR, filename)
    with open(file_path, "w") as f:
        f.write(data)
    print(f"Saved log to {file_path}")

def save_results_table(results, filename="tsp_results.csv"):
    """
    {
        "summary": "Saves a table of results (e.g., path cost comparisons) to a CSV file.",
        "parameters": {
            "results": "list of dict - A list of dictionaries where each dict is a row in the results table.",
            "filename": "str - The name of the CSV file (default is 'tsp_results.csv')."
        },
        "output": "A .csv file is saved in the 'tables' directory.",
        "prints": "The full file path where the CSV file is saved."
    }
    """
    import pandas as pd
    df = pd.DataFrame(results)
    file_path = os.path.join(TABLES_DIR, filename)
    df.to_csv(file_path, index=False)
    print(f"Saved results table to {file_path}")
