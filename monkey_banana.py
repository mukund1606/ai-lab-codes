class State:
    def __init__(self, monkey_location, boxes_on_floor, boxes_stacked, has_bananas):
        self.monkey_location = monkey_location
        self.boxes_on_floor = boxes_on_floor
        self.boxes_stacked = boxes_stacked
        self.has_bananas = has_bananas

    def __eq__(self, other):
        return (
            self.monkey_location == other.monkey_location
            and self.boxes_on_floor == other.boxes_on_floor
            and self.boxes_stacked == other.boxes_stacked
            and self.has_bananas == other.has_bananas
        )

    def __hash__(self):
        return hash(
            (
                self.monkey_location,
                tuple(self.boxes_on_floor),
                tuple(self.boxes_stacked),
                self.has_bananas,
            )
        )


class MonkeyBananaProblem:
    def __init__(self, initial_state, max_boxes):
        self.initial_state = initial_state
        self.max_boxes = max_boxes

    def actions(self, state):
        possible_actions = []
        if state.monkey_location == "A":
            possible_actions.append("move_to_B")
        elif state.monkey_location == "B":
            possible_actions.append("move_to_A")
            if state.boxes_on_floor:
                possible_actions.append("stack_box")
        if state.boxes_stacked:
            possible_actions.append("unstack_box")
            if state.monkey_location == "A" and not state.has_bananas:
                possible_actions.append("grab_bananas")
        return possible_actions

    def result(self, state, action):
        new_state = State(
            state.monkey_location,
            state.boxes_on_floor[:],
            state.boxes_stacked[:],
            state.has_bananas,
        )
        if action == "move_to_B":
            new_state.monkey_location = "B"
        elif action == "move_to_A":
            new_state.monkey_location = "A"
        elif action == "stack_box":
            if len(new_state.boxes_stacked) < self.max_boxes:
                new_state.boxes_stacked.append(new_state.boxes_on_floor.pop())
        elif action == "unstack_box":
            new_state.boxes_on_floor.append(new_state.boxes_stacked.pop())
        elif action == "grab_bananas":
            new_state.has_bananas = True
        return new_state

    def goal_test(self, state):
        return state.has_bananas


def dfs(problem, state, path=[]):
    if problem.goal_test(state):
        return path
    for action in problem.actions(state):
        new_state = problem.result(state, action)
        if new_state not in path:
            new_path = dfs(problem, new_state, path + [new_state])
            if new_path:
                return new_path
    return None


# Define initial state
initial_state = State("A", ["box1", "box2"], [], False)
# Define max number of boxes that can be stacked
max_boxes = 2
# Create monkey banana problem instance
problem = MonkeyBananaProblem(initial_state, max_boxes)
# Solve the problem
solution = dfs(problem, initial_state)
if solution:
    print("Solution found:")
    for state in solution:
        print(
            f"Monkey is at {state.monkey_location}, boxes on floor: {state.boxes_on_floor}, "
            f"boxes stacked: {state.boxes_stacked}, has bananas: {state.has_bananas}"
        )
else:
    print("No solution found.")
