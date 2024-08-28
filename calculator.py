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