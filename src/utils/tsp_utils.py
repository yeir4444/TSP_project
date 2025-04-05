import pandas as pd

def load_distance_matrix(filepath):
    """
    {
        "summary": "Loads the distance matrix from a CSV file.",
        "parameters": {
            "filepath": "str - Path to the CSV file containing the distance matrix."
        },
        "returns": "np.array - 2D distance matrix."
    }
    """
    return pd.read_csv(filepath).to_numpy()

def compute_tour_length(tour, distances):
    """
    {
        "summary": "Computes the total distance of a complete TSP tour.",
        "parameters": {
            "tour": "list - Ordered list of cities representing the tour.",
            "distances": "np.array - Distance matrix between cities."
        },
        "returns": "float - Total length of the tour."
    }
    """
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1)) + distances[tour[-1], tour[0]]
