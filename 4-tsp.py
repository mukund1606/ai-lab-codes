import sys


def tsp(weights):
    n = len(weights)

    # Initialize the dynamic programming table with a large value indicating unvisited states
    dp = [[sys.maxsize] * n for _ in range(2**n)]

    # Initialize base case
    dp[1][0] = 0  # Starting from city 0

    for mask in range(1, 2**n):
        for j in range(n):
            if mask & (1 << j):
                for k in range(n):
                    if (
                        mask & (1 << k)
                        and k != j
                        and dp[mask ^ (1 << j)][k] != sys.maxsize
                    ):
                        dp[mask][j] = min(
                            dp[mask][j], dp[mask ^ (1 << j)][k] + weights[k][j]
                        )

    # Finding the shortest path
    min_dist = sys.maxsize
    last_city = None
    for j in range(1, n):
        if (
            dp[2**n - 1][j] != sys.maxsize
            and min_dist > dp[2**n - 1][j] + weights[j][0]
        ):
            min_dist = dp[2**n - 1][j] + weights[j][0]
            last_city = j

    # Reconstructing the path
    path = [0]
    mask = 2**n - 1
    while mask != 1:  # Stop when all cities have been visited
        for k in range(n):
            if (
                mask & (1 << k)
                and k != last_city
                and dp[mask][last_city]
                == dp[mask ^ (1 << last_city)][k] + weights[k][last_city]
            ):
                path.append(last_city)
                mask ^= 1 << last_city
                last_city = k
                break

    path.append(0)  # Add the starting city to complete the path
    return path[::-1], min_dist  # Reverse the path to start from the initial city


def print_path_and_distance(path, distance, weights):
    print("Shortest path:", path)
    print("Distance:", distance)


if __name__ == "__main__":
    # Example weighted matrix representing distances between cities
    weights = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

    shortest_path, shortest_distance = tsp(weights)
    print_path_and_distance(shortest_path, shortest_distance, weights)
