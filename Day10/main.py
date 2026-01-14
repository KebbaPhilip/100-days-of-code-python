import art
def add(n1, n2):
    """add two numbers n1, n2 and return the result"""
    return n1 + n2

def subtract(n1, n2):
    """subtracts two numbers n1, n2 and return the result"""
    return n1 - n2

def multiply(n1, n2):
    """multiplies two numbers n1, n2 and return the result"""
    return n1 * n2

def divide(n1, n2):
    """divides two numbers n1, n2 and returns the result"""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    num1 = float(input("What is the first number?: "))
    while True:
        for symbol in operations:
            print(symbol)

        operator = input("Pick an operation: ")
        num2 = float(input("What is the next number: "))

        operation_function = operations[operator]
        result = operation_function(num1, num2)
        print(f"{num1} {operator} {num2} = { result}")

        continue_calc = input(f"Type 'y' to continue working with {result}, or type 'n' to start a new calculation:  ").lower()

        if continue_calc == "y":
            num1 = result
        elif continue_calc == "n":
            calculator()


calculator()









