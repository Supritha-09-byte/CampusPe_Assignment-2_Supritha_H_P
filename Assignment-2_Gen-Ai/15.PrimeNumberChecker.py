"""
Question 15: Prime Number Checker

Part 1:
Check whether a single number is prime.
Handle negative numbers, 0, 1, and 2.

Part 2:
Find all prime numbers in a given range.
"""

import math  # Used for square root optimization


# Function to check if a number is prime
def is_prime(number):
    """
    Returns True if number is prime.
    Returns False otherwise.
    """

    # Handle negative numbers, 0 and 1
    if number <= 1:
        return False

    # 2 is the only even prime number
    if number == 2:
        return True

    # Eliminate even numbers greater than 2
    if number % 2 == 0:
        return False

    # Check divisibility from 3 to sqrt(number)
    # We use sqrt optimization for better efficiency
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False

    return True


# Main program
def prime_number_program():

    print("===== PRIME NUMBER CHECKER =====\n")

    try:
        # -------------------------
        # Part 1: Single Number Check
        # -------------------------
        number = int(input("Enter a number: "))

        if is_prime(number):
            print(f"{number} is a PRIME number")
        else:
            print(f"{number} is NOT a prime number")

        # -------------------------
        # Part 2: Range Prime Finder
        # -------------------------
        start_range = int(input("\nEnter start range: "))
        end_range = int(input("Enter end range: "))

        # Validate range
        if start_range > end_range:
            print("Start range cannot be greater than end range.")
            return

        prime_numbers = []  # List to store primes in range

        # Loop through range
        for num in range(start_range, end_range + 1):
            if is_prime(num):
                prime_numbers.append(num)

        # Display results
        print("\nPrime numbers:", end=" ")

        if prime_numbers:
            print(", ".join(map(str, prime_numbers)))
        else:
            print("No prime numbers found in this range.")

    except ValueError:
        print(" Invalid input! Please enter integers only.")


# Run the program
if __name__ == "__main__":
    prime_number_program()