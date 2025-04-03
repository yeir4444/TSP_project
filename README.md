# Traveling Salesman Problem (TSP) Solver

This project solves the **Traveling Salesman Problem (TSP)** using multiple optimization algorithms:
- **Ant Colony Optimization (ACO)**
- **Genetic Algorithm (GA)**

The implementation includes visualization tools to plot solutions and save results in a structured manner.

---

## 📁 Project Structure
```
TSP_Project/
│── data/
│   ├── city_distances.csv  # Distance matrix for cities
│   ├── city_distances_extended.csv  # Extended version of Distance matrix for cities
│── src/
│   ├── algorithms/
│   │   ├── aco.py  # Ant Colony Optimization
│   │   ├── ga.py  # Genetic Algorithm
│   ├── utils/
│   │   ├── visualization.py  # Visualization functions
│   │   ├── tsp_utils.py  # TSP functions
│   ├── main.py  # Entry point for running the TSP solver
│── results/
│   ├── figures/  # Saved TSP solution plots
│   ├── log/  # Algorithm logs (best paths & distances)
│   ├── tables/  # Comparison results in CSV format
│── requirements.txt  # Required Python libraries
│── README.md  # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yeir4444/TSP_project
cd TSP_Project
```

### 2️⃣ **Install Dependencies**
Ensure you have Python installed. Then, install required libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the Program**
Navigate to the `src/` directory and execute the script:
```bash
cd src
python main.py
```

---

## 🖼️ Output & Results
Upon execution, the program will:
✅ Compute the best TSP routes using ACO and GA.
✅ Save **TSP solution plots** in `results/figures/`
✅ Save **algorithm logs** (best path & distances) in `results/log/`
✅ Save **comparison results** in `results/tables/`

Example outputs:
- `results/figures/aco_solution.png`
- `results/log/aco_log.txt`
- `results/tables/tsp_comparison.csv`

---

## 📌 Notes
- The program assumes `data/city_distances.csv` and  `data/city_distances_extended.csv` contains a **distance matrix**.
