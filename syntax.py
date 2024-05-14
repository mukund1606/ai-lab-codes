def check_syntax(code):
    try:
        compile(code, "<string>", "exec")
        print("Syntax is correct.")
    except SyntaxError as e:
        print(f"Syntax error: {e}")


# Example usage:
code_to_check = """
def my_function():
    print("Hello, world!")
"""

check_syntax(code_to_check)
