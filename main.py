import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    should_continue = True
    n1 = float(input("What's the first number?: "))

    while should_continue:
        for key in operations:
            print(key)
        operand = input("\nPick an operation: ")
        n2 = float(input("What's the next number?: "))
        result = operations[operand](n1, n2)
        print(f"{n1} {operand} {n2} = {result}")

        choice = input(f"Type \"y\" to continue calculating with {result}, or type \"n\" to start a new calculation: ").lower()

        if choice == "y":
            n1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()