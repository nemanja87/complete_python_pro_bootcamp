import art

def calculator():
    print(art.logo)

    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    def multiple(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return  n1 / n2

    all_operations = {
        "+": add,
        "-": sub,
        "*": multiple,
        "/": divide
    }

    is_on = "y"
    result = 0
    first_number = float(input("What is the first number? "))

    while is_on != "n":
        operation = input("Pick an operation? + - * / ")
        second_number = float(input("What is the second number? "))

        result = all_operations[operation](first_number, second_number)

        is_on = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ").lower()

        if is_on == "y":
            first_number = result
        else:
            calculator()

calculator()