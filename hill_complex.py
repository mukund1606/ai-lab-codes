import random
import numpy as np
import matplotlib.pyplot as plt


# Define a more complex objective function
def complex_objective_function(x, y):
    return (x - 3) ** 2 + (y + 2) ** 2 + np.sin(x * y)


# Define the hill climbing algorithm with the option for both minimization and maximization
def hill_climbing(obj_func, bounds, step_size, max_iterations, maximize=False):
    best_solution = [
        random.uniform(bounds[i][0], bounds[i][1]) for i in range(len(bounds))
    ]
    best_score = obj_func(*best_solution)

    solution_history = [
        best_solution
    ]  # Store the history of solutions for visualization

    for _ in range(max_iterations):
        # Generate a new candidate solution by adding a random value to each dimension of the current solution
        candidate_solution = [
            best_solution[i] + random.uniform(-step_size, step_size)
            for i in range(len(bounds))
        ]

        # Clip the candidate solution to ensure it stays within bounds
        candidate_solution = [
            min(max(candidate_solution[i], bounds[i][0]), bounds[i][1])
            for i in range(len(bounds))
        ]

        # Calculate the objective function value for the candidate solution
        candidate_score = obj_func(*candidate_solution)

        # Update the best solution if the candidate solution is better
        if (maximize and candidate_score > best_score) or (
            not maximize and candidate_score < best_score
        ):
            best_solution = candidate_solution
            best_score = candidate_score
            solution_history.append(best_solution)

    return best_solution, best_score, solution_history


# Visualize the search process
def visualize_search(obj_func, bounds, solution_history):
    x = np.linspace(bounds[0][0], bounds[0][1], 100)
    y = np.linspace(bounds[1][0], bounds[1][1], 100)
    X, Y = np.meshgrid(x, y)
    Z = obj_func(X, Y)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)

    solution_history = np.array(solution_history)
    ax.scatter(
        solution_history[:, 0],
        solution_history[:, 1],
        [obj_func(*point) for point in solution_history],
        color="red",
        s=100,
        label="Search Path",
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Objective Function Value")
    ax.set_title("Hill Climbing Search")
    ax.legend()

    plt.show()


# Example usage
if __name__ == "__main__":
    # Define parameters
    bounds = [(-10, 10), (-5, 5)]  # Bounds for each dimension
    step_size = 0.5
    max_iterations = 100

    # Run hill climbing algorithm for minimization
    best_solution, best_score, solution_history = hill_climbing(
        complex_objective_function, bounds, step_size, max_iterations
    )

    # Print results
    print("Best solution found:", best_solution)
    print("Objective function value at best solution:", best_score)

    # Visualize the search process
    visualize_search(complex_objective_function, bounds, solution_history)
