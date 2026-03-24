"""
Assignment - Arithmetic Operations
Description: Program to perform basic mathematical operations on two numbers.
"""

def perform_calculations():
    print("===== Arithmetic Calculator =====\n")

    try:
        # Taking input from user
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        print("\nResults:")

        # Addition
        print(f"{first_number} + {second_number} = {first_number + second_number}")

        # Subtraction
        print(f"{first_number} - {second_number} = {first_number - second_number}")

        # Multiplication
        print(f"{first_number} * {second_number} = {first_number * second_number}")

        # Division (check for division by zero)
        if second_number != 0:
            division_result = first_number / second_number
            print(f"{first_number} / {second_number} = {division_result:.2f}")
        else:
            print(f"{first_number} / {second_number} = Cannot divide by zero")

        # Modulus
        if second_number != 0:
            print(f"{first_number} % {second_number} = {first_number % second_number}")
        else:
            print(f"{first_number} % {second_number} = Cannot perform modulus by zero")

        # Exponentiation
        print(f"{first_number} ^ {second_number} = {first_number ** second_number}")

    except ValueError:
        print("\n Invalid input! Please enter numeric values only.")


# Main execution
if __name__ == "__main__":
    perform_calculations()