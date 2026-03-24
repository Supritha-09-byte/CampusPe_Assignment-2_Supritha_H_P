"""
Question 20: Number System Functions

Description:
This program implements various mathematical utility functions
and provides a menu to test them individually.
"""


# 1. Factorial function
def factorial(n):
    """Returns factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 2. Prime check function
def is_prime(n):
    """Returns True if n is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# 3. Fibonacci function (nth Fibonacci number)
def fibonacci(n):
    """Returns nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# 4. Sum of digits
def sum_of_digits(n):
    """Returns sum of digits of n."""
    return sum(int(digit) for digit in str(abs(n)))


# 5. Reverse number
def reverse_number(n):
    """Returns reversed number."""
    reversed_num = int(str(abs(n))[::-1])
    return -reversed_num if n < 0 else reversed_num


# 6. Armstrong number check
def is_armstrong(n):
    """Checks if n is an Armstrong number."""
    digits = str(abs(n))
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == abs(n)


# 7. GCD using Euclidean Algorithm
def gcd(a, b):
    """Returns greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


# 8. LCM using GCD
def lcm(a, b):
    """Returns least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# 9. Perfect number check
def is_perfect_number(n):
    """Checks if n is a perfect number."""
    if n <= 1:
        return False

    total = 1  # 1 is always a divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    return total == n


# 10. Menu function
def math_menu():
    """Displays menu to test mathematical functions."""

    while True:
        print("\nNUMBER SYSTEM FUNCTIONS MENU")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice (1-10): "))

            if choice == 10:
                print("Exiting program.")
                break

            if choice == 1:
                n = int(input("Enter a number: "))
                print("Factorial:", factorial(n))

            elif choice == 2:
                n = int(input("Enter a number: "))
                print("Prime:", is_prime(n))

            elif choice == 3:
                n = int(input("Enter position (n): "))
                print("Fibonacci:", fibonacci(n))

            elif choice == 4:
                n = int(input("Enter a number: "))
                print("Sum of digits:", sum_of_digits(n))

            elif choice == 5:
                n = int(input("Enter a number: "))
                print("Reversed number:", reverse_number(n))

            elif choice == 6:
                n = int(input("Enter a number: "))
                print("Armstrong:", is_armstrong(n))

            elif choice == 7:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == 8:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == 9:
                n = int(input("Enter a number: "))
                print("Perfect Number:", is_perfect_number(n))

            else:
                print("Invalid choice.")

        except ValueError as error:
            print("Error:", error)


# Run program
if __name__ == "__main__":
    math_menu()