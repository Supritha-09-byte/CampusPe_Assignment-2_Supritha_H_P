"""
Question 11: Number Pattern Printer
Description: Prints different number patterns based on user choice.
"""

def print_pattern(pattern_choice, height):
    
    if pattern_choice == 1:
        # Pattern 1
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif pattern_choice == 2:
        # Pattern 2
        for i in range(1, height + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    elif pattern_choice == 3:
        # Pattern 3
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    elif pattern_choice == 4:
        # Pattern 4
        for i in range(1, height + 1):
            # Ascending part
            for j in range(1, i + 1):
                print(j, end="")
            # Descending part
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    else:
        print(" Invalid pattern choice!")


def number_pattern_printer():
    print("===== NUMBER PATTERN PRINTER =====")

    while True:
        try:
            print("\nChoose Pattern:")
            print("1. Increasing Numbers")
            print("2. Repeated Numbers")
            print("3. Reverse Decreasing")
            print("4. Palindrome Pattern")
            print("5. Exit")

            choice = int(input("Enter your choice (1-5): "))

            if choice == 5:
                print("Exiting program... Goodbye!")
                break

            if choice < 1 or choice > 5:
                print(" Please select between 1 and 5.")
                continue

            height = int(input("Enter height: "))

            if height <= 0:
                print(" Height must be greater than 0.")
                continue

            print("\nGenerated Pattern:\n")
            print_pattern(choice, height)

        except ValueError:
            print("Invalid input! Please enter numeric values.")


# Main execution
if __name__ == "__main__":
    number_pattern_printer()