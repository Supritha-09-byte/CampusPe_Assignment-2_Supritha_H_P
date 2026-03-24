"""
Question 14: Factorial Calculator
Description:
This program calculates the factorial of a number using a loop.
It handles:
- Zero case (0! = 1)
- Negative numbers (not allowed)
- Displays step-by-step multiplication
"""

def factorial_calculator():

    print("===== FACTORIAL CALCULATOR =====\n")

    try:
        # Ask user to enter a number
        number = int(input("Enter a number: "))

        # Handle negative number case
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return

        # Handle zero case
        if number == 0:
            print("0! = 1")
            return

        # Initialize factorial result
        factorial_result = 1

        # String to store step-by-step calculation
        steps = ""

        # Loop from number down to 1
        for i in range(number, 0, -1):
            factorial_result *= i  # Multiply each number

            # Build step-by-step string
            steps += str(i)
            if i != 1:
                steps += " × "

        # Display final result
        print(f"\n{number}! = {steps} = {factorial_result}")

    except ValueError:
        # Handle non-numeric input
        print(" Invalid input! Please enter a valid integer.")


# Main execution block
if __name__ == "__main__":
    factorial_calculator()