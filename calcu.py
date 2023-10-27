def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

print("Simple Calculator")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    try:
        choice = int(input("Enter choice (1/2/3/4): "))

        if choice not in [1, 2, 3, 4]:
            print("Invalid input. Please try again.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = add(num1, num2)
            print("Result:", result)
        elif choice == 2:
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == 3:
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == 4:
            result = divide(num1, num2)
            print("Result:", result)
        
        break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
