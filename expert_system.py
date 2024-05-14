# Define facts
facts = {"age": lambda: 1, "citizenship": lambda: "US Citizen"}

# Define comparison functions
comparison_functions = {
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y,
    ">=": lambda x, y: x >= y,
    ">": lambda x, y: x > y,
    "<=": lambda x, y: x <= y,
    "<": lambda x, y: x < y,
}

# Define rules
rules = [
    {
        "conditions": [
            {"fact": "age", "comparison": ">=", "value": 18},
            {"fact": "citizenship", "comparison": "==", "value": "US Citizen"},
        ],
        "conclusion": "Eligible to vote",
    },
    {
        "conditions": [{"fact": "age", "comparison": "<", "value": 18}],
        "conclusion": "Not eligible to vote",
    },
    {
        "conditions": [
            {"fact": "citizenship", "comparison": "!=", "value": "US Citizen"}
        ],
        "conclusion": "Not eligible to vote",
    },
]

# Check rules
for rule in rules:
    is_rule_satisfied = all(
        comparison_functions[condition["comparison"]](
            facts[condition["fact"]](), condition["value"]
        )
        for condition in rule["conditions"]
    )
    if is_rule_satisfied:
        print(rule["conclusion"])
        break
else:
    print("No conclusion found")
