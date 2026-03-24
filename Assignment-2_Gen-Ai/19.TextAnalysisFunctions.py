"""
Question 19: Text Analysis Functions

Description:
This program performs various text analysis operations using
separate modular functions.
"""

import string  # Used to handle punctuation removal


# Function 1: Count number of words
def count_words(text):
    """
    Returns total number of words in text.
    """
    words = text.split()
    return len(words)


# Function 2: Count number of vowels
def count_vowels(text):
    """
    Returns total number of vowels in text.
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


# Function 3: Count number of consonants
def count_consonants(text):
    """
    Returns total number of consonants in text.
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in vowels:
            count += 1
    return count


# Function 4: Reverse text
def reverse_text(text):
    """
    Returns reversed version of text.
    """
    return text[::-1]


# Function 5: Check palindrome
def is_palindrome(text):
    """
    Returns True if text is palindrome (ignores case and spaces).
    """
    processed = text.lower().replace(" ", "")
    return processed == processed[::-1]


# Function 6: Remove vowels
def remove_vowels(text):
    """
    Returns text with all vowels removed.
    """
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


# Function 7: Word frequency dictionary
def word_frequency(text):
    """
    Returns dictionary of word frequencies (case insensitive).
    """
    # Remove punctuation
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))

    words = cleaned_text.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# Function 8: Find longest word
def longest_word(text):
    """
    Returns longest word and its length.
    """
    cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
    words = cleaned_text.split()

    if not words:
        return "", 0

    longest = max(words, key=len)
    return longest, len(longest)


# Function 9: Analyze text (Main function)
def analyze_text(text):
    """
    Calls all text analysis functions and displays results.
    """

    print("\n=== TEXT ANALYSIS ===")

    print(f"Words: {count_words(text)}")
    print(f"Vowels: {count_vowels(text)}")
    print(f"Consonants: {count_consonants(text)}")
    print(f"Reversed: {reverse_text(text)}")

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print(f"Without vowels: {remove_vowels(text)}")

    longest, length = longest_word(text)
    print(f"Longest word: {longest} ({length} letters)")

    frequency = word_frequency(text)

    # Format frequency output
    formatted_frequency = ", ".join([f"{word}: {count}" for word, count in frequency.items()])
    print(f"Word Frequency: {formatted_frequency}")


# Main execution block
if __name__ == "__main__":
    user_text = input("Enter text: ")
    analyze_text(user_text)