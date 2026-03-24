"""
Question 12: Multiplication Table Generator
Description:
This program allows the user to:
1. Generate multiplication table for a specific number and range.
2. Generate a full multiplication table grid (1–10).
"""

# Function to generate a single multiplication table
def generate_single_table():
    try:
        # Ask user for number
        number = int(input("Enter number: "))
        
        # Ask user for range limit
        end_range = int(input("Enter range (end): "))

        # Validate range
        if end_range <= 0:
            print(" Range must be greater than 0.")
            return

        # Display heading
        print(f"\nMultiplication Table of {number}\n")

        # Loop from 1 to given range
        for i in range(1, end_range + 1):
            result = number * i  # Calculate multiplication
            print(f"{number} x {i} = {result}")

    # Handle invalid input (non-numeric)
    except ValueError:
        print(" Invalid input! Please enter numeric values.")


# Function to generate full multiplication table (1–10 grid)
def generate_full_table():
    
    print("\n===== FULL MULTIPLICATION TABLE (1-10) =====\n")

    # Print header row
    print("     ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print()

    # Print separator line
    print("-" * 55)

    # Outer loop for rows (1–10)
    for i in range(1, 11):
        print(f"{i:2} |", end="")

        # Inner loop for columns (1–10)
        for j in range(1, 11):
            product = i * j  # Calculate product
            print(f"{product:4}", end="")
        print()


# Main menu function
def multiplication_table_program():

    while True:
        # Display menu options
        print("\n===== MULTIPLICATION TABLE GENERATOR =====")
        print("1. Generate Single Table")
        print("2. Generate Full Table (1-10)")
        print("3. Exit")

        try:
            # Take menu choice
            choice = int(input("Enter your choice: "))

            # Call single table function
            if choice == 1:
                generate_single_table()

            # Call full grid function
            elif choice == 2:
                generate_full_table()

            # Exit program
            elif choice == 3:
                print("Exiting program... Goodbye!")
                break

            # Invalid choice handling
            else:
                print(" Invalid choice! Please select 1, 2, or 3.")

        except ValueError:
            print(" Please enter a valid number.")


# This ensures the program runs only when executed directly
if __name__ == "__main__":
    multiplication_table_program()