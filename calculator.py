from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("Cannot divide by zero")


calculations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(logo)
    first_number = float(input("Enter first number: \n"))
    accumulate = True

    while accumulate:

        user_operation = input("Select operation. '+', '-', '*' or '/': \n")
        second_number = float(input("Enter second number: \n"))
        result = calculations[user_operation](first_number, second_number)
        if result is None:
            result = 0
        print(f"{first_number} {user_operation} {second_number} = {result}")

        calculate_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if calculate_again == "n":
            accumulate = False
            print("\n" * 20)
            calculator()
        else:
            first_number = result


calculator()