import re


def convert_predicate_to_propositional(expression):
    # Define a dictionary to store variable mappings
    variable_map = {}
    next_variable_index = 0

    def replace_variables(match):
        nonlocal next_variable_index
        variable = match.group(1)
        if variable not in variable_map:
            variable_map[variable] = f"P{next_variable_index}"
            next_variable_index += 1
        return variable_map[variable]

    # Replace variables with propositional variables
    expression = re.sub(r"([a-zA-Z]+)\((\w+)\)", replace_variables, expression)

    # Replace quantifiers with placeholders
    expression = re.sub(r"∀([a-zA-Z]+)", r"", expression)
    expression = re.sub(r"∃([a-zA-Z]+)", r"", expression)

    # Correct the logical connectives
    expression = re.sub(r"(\w+) ∧ (\w+)", r"\1∧\2", expression)
    expression = re.sub(r"(\w+) ∨ (\w+)", r"\1∨\2", expression)

    # Replace placeholders with propositional variables
    for variable, placeholder in variable_map.items():
        expression = expression.replace(f"∀_{variable}", f"({placeholder})")
        expression = expression.replace(f"∃_{variable}", f"({placeholder})")

    return expression


# Example usage
predicate_logic_expression = "∀x (P(x) ∧ Q(x)) ∨ ∃y R(y)"
propositional_logic_expression = convert_predicate_to_propositional(
    predicate_logic_expression
)
print("Predicate Logic Expression:", predicate_logic_expression)
print("Propositional Logic Expression:", propositional_logic_expression)
