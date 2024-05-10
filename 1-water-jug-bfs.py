from collections import deque


# Function to perform BFS to find the solution
def water_jug_bfs(capacity_A, capacity_B, target):
    # Queue to store states during BFS
    queue = deque()
    # Set to store visited states
    visited = set()

    # Initial state
    initial_state = (0, 0)
    queue.append((initial_state, []))
    visited.add(initial_state)

    # Perform BFS
    while queue:
        current_state, path = queue.popleft()
        a, b = current_state

        # Check if target is reached
        if a == target or b == target:
            print("Solution found!")
            print("Steps to reach the solution:")
            for step, (a_amount, b_amount) in zip(
                path, path_to_states(path, capacity_A, capacity_B)
            ):
                print(step, "- Jug A:", a_amount, "Jug B:", b_amount)
            return True

        # Actions: Fill jug A, Fill jug B, Empty jug A, Empty jug B,
        #           Pour from A to B, Pour from B to A
        actions = [
            ("Fill A", (capacity_A, b)),
            ("Fill B", (a, capacity_B)),
            ("Empty A", (0, b)),
            ("Empty B", (a, 0)),
            ("Pour A to B", (max(0, a - (capacity_B - b)), min(b + a, capacity_B))),
            ("Pour B to A", (min(a + b, capacity_A), max(0, b - (capacity_A - a)))),
        ]

        for action_name, next_state in actions:
            if next_state not in visited:
                queue.append((next_state, path + [action_name]))
                visited.add(next_state)

    # If BFS is completed and no solution found
    print("No solution found!")
    return False


# Function to convert path to states
def path_to_states(path, capacity_A, capacity_B):
    states = [(0, 0)]
    for action in path:
        prev_a, prev_b = states[-1]
        if action == "Fill A":
            states.append((capacity_A, prev_b))
        elif action == "Fill B":
            states.append((prev_a, capacity_B))
        elif action == "Empty A":
            states.append((0, prev_b))
        elif action == "Empty B":
            states.append((prev_a, 0))
        elif action == "Pour A to B":
            a_to_b = min(prev_a, capacity_B - prev_b)
            states.append((prev_a - a_to_b, prev_b + a_to_b))
        elif action == "Pour B to A":
            b_to_a = min(prev_b, capacity_A - prev_a)
            states.append((prev_a + b_to_a, prev_b - b_to_a))
    return states[1:]


# Example usage:
jug_A_capacity = 4
jug_B_capacity = 3
target_amount = 2
water_jug_bfs(jug_A_capacity, jug_B_capacity, target_amount)
