import pandas as pd

def load_distance_matrix(filepath):
    return pd.read_csv(filepath).to_numpy()

def compute_tour_length(tour, distances):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1)) + distances[tour[-1], tour[0]]


