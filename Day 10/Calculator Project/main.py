import art
print(art.logo)

def add(n1, n2):
    """Add two inputs together,result exist in boolean data type."""

    return n1 + n2

def sub(n1, n2):
    """Subtracts two inputs,result exist in boolean data type."""

    return n1 - n2

def mul(n1, n2):
    """Multiplies two inputs,result exist in boolean data type."""
    return n1 * n2

def div(n1, n2):
    """Divides two inputs together,result exist in boolean data type."""
    return n1 / n2

def calculator():
    n1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue:
        print("+\n-\n*\n/")
        operator = input("Pick an operation?: ")
        n2 = float(input("What's the next number?: "))

        if operator == "+":
            result = add(n1, n2)
        elif operator == "-":
            result = sub(n1, n2)
        elif operator == "*":
            result = mul(n1, n2)
        elif operator == "/":
            result = div(n1, n2)
        else:
            print("Invalid Operator")
            continue

        print(f"Your result is {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            n1 = result
        elif choice == "n":
            should_continue = False
            calculator()
        else:
            print("Invalid response")

calculator()