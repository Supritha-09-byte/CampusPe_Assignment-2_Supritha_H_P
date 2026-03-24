"""
Question 18: Calculator Using Functions

Description:
This program implements a calculator using separate functions
for each arithmetic operation.

Functions:
1. add(a, b)
2. subtract(a, b)
3. multiply(a, b)
4. divide(a, b)
5. modulus(a, b)
6. power(a, b)
7. calculator() - main menu function
"""


# Function to perform addition
def add(a, b):
    return a + b


# Function to perform subtraction
def subtract(a, b):
    return a - b


# Function to perform multiplication
def multiply(a, b):
    return a * b


# Function to perform division
def divide(a, b):
    # Handle division by zero
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# Function to perform modulus operation
def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b


# Function to perform exponentiation
def power(a, b):
    return a ** b


# Main calculator function
def calculator():

    while True:
        print("\nCALCULATOR MENU")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        try:
            # Take user choice
            choice = int(input("Enter your choice (1-7): "))

            # Exit condition
            if choice == 7:
                print("Exiting calculator.")
                break

            # Validate choice range
            if choice < 1 or choice > 7:
                print("Invalid choice. Please select between 1 and 7.")
                continue

            # Take numeric inputs
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Call appropriate function based on choice
            if choice == 1:
                result = add(num1, num2)
            elif choice == 2:
                result = subtract(num1, num2)
            elif choice == 3:
                result = multiply(num1, num2)
            elif choice == 4:
                result = divide(num1, num2)
            elif choice == 5:
                result = modulus(num1, num2)
            elif choice == 6:
                result = power(num1, num2)

            # Display result
            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values only.")


# Run the program
if __name__ == "__main__":
    calculator()