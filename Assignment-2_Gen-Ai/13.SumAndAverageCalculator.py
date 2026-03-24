"""
Question 13: Sum and Average Calculator
Description:
This program asks the user how many numbers they want to enter.
It then calculates:
1. Sum
2. Average
3. Maximum number
4. Minimum number
"""

def sum_average_calculator():

    print("===== SUM AND AVERAGE CALCULATOR =====\n")

    try:
        # Ask user how many numbers they want to enter
        count = int(input("How many numbers? "))

        # Validate input
        if count <= 0:
            print("Number of inputs must be greater than 0.")
            return

        numbers = []  # List to store all numbers

        # Loop to take 'count' numbers from user
        for i in range(1, count + 1):
            number = float(input(f"Enter number {i}: "))
            numbers.append(number)  # Store number in list

        # Calculate sum using built-in function
        total_sum = sum(numbers)

        # Calculate average
        average = total_sum / count

        # Find maximum and minimum using built-in functions
        maximum_number = max(numbers)
        minimum_number = min(numbers)

        # Display results
        print("\n===== RESULTS =====")
        print(f"Sum: {total_sum}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum_number}")
        print(f"Minimum: {minimum_number}")

    except ValueError:
        # Handle non-numeric input
        print(" Invalid input! Please enter numeric values only.")


# Main execution block
if __name__ == "__main__":
    sum_average_calculator()