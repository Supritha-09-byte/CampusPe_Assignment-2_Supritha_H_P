"""
Question 17: Palindrome Checker

Description:
This program checks whether a given word or number
is a palindrome (reads the same forwards and backwards).

Features:
- Ignores case for words
- Works for numbers
- Displays original value
- Displays reversed value
- Shows step-by-step verification
"""

def palindrome_checker():

    print("PALINDROME CHECKER\n")

    # Take input from user
    user_input = input("Enter word/number: ").strip()

    # Store original input
    original_value = user_input

    # Convert to lowercase for case-insensitive comparison
    processed_value = user_input.lower()

    # Reverse the processed value using slicing
    reversed_value = processed_value[::-1]

    # Display original and reversed values
    print(f"\nOriginal: {original_value}")
    print(f"Reversed: {original_value[::-1]}")

    print("\nStep-by-step comparison:")

    # Compare characters one by one
    is_palindrome = True
    length = len(processed_value)

    for i in range(length // 2):
        print(f"Comparing '{processed_value[i]}' and '{processed_value[length - i - 1]}'")

        if processed_value[i] != processed_value[length - i - 1]:
            is_palindrome = False
            break

    # Display result
    if is_palindrome:
        print("\nResult: PALINDROME")
    else:
        print("\nResult: NOT A PALINDROME")


# Main execution
if __name__ == "__main__":
    palindrome_checker()