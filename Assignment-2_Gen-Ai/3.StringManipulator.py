"""
Question 3: String Manipulator
Description: Performs various string operations on a user-entered sentence.
"""

def string_manipulator():
    print("===== STRING MANIPULATOR =====\n")

    try:
        # Taking sentence input
        user_sentence = input("Enter a sentence: ").strip()

        # Check if input is empty
        if not user_sentence:
            raise ValueError("Sentence cannot be empty.")

        # 1. Original sentence
        original_sentence = user_sentence

        # 2. Total characters (with spaces)
        characters_with_spaces = len(user_sentence)

        # 3. Total characters (without spaces)
        characters_without_spaces = len(user_sentence.replace(" ", ""))

        # 4. Total words
        word_list = user_sentence.split()
        total_words = len(word_list)

        # 5. Uppercase
        uppercase_sentence = user_sentence.upper()

        # 6. Lowercase
        lowercase_sentence = user_sentence.lower()

        # 7. Title Case
        title_case_sentence = user_sentence.title()

        # 8. First word
        first_word = word_list[0]

        # 9. Last word
        last_word = word_list[-1]

        # 10. Reversed sentence
        reversed_sentence = user_sentence[::-1]

        # Display results
        print("\nResults:")
        print(f"Original: {original_sentence}")
        print(f"Characters (with spaces): {characters_with_spaces}")
        print(f"Characters (without spaces): {characters_without_spaces}")
        print(f"Words: {total_words}")
        print(f"UPPERCASE: {uppercase_sentence}")
        print(f"lowercase: {lowercase_sentence}")
        print(f"Title Case: {title_case_sentence}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Reversed: {reversed_sentence}")

    except ValueError as error:
        print("\n Error:", error)


# Main execution
if __name__ == "__main__":
    string_manipulator()