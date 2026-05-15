from art import logo
def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# TODO: Use the dictionary operations to perform the calculations, Multiply 4 * 8 using the dictionary.
# calculate = operations["*"]
# print(calculate(first_number, second_number))
# print(operations["*"](4,8))

def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    continue_running = True
    while continue_running:
        for keys in operations:
            print(keys)
        operators = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        output = operations[operators](first_number, second_number)
        print(f"{first_number} {operators} {second_number} = {output}")
        asking_for_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()
        if asking_for_continue == 'y':
            first_number = output
        else:
            continue_running = False
            print("\n" * 20)
            calculator()

calculator()
