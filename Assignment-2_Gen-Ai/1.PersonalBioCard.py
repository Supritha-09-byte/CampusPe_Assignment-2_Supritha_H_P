"""
Assignment 2 - GENAI
Question 1: Personal Bio Card
Author: Supritha H P
"""

def create_bio_card():

    full_name = "Supritha H P"
    age = 21
    course_name = "Generative AI"
    college_name = "SJB Institute of Technology"
    email_address = "suprithahp04@gmail.com"

    # Store all lines in a list
    bio_lines = [
        f"Name    : {full_name}",
        f"Age     : {age} years",
        f"Course  : {course_name}",
        f"College : {college_name}",
        f"Email   : {email_address}"
    ]

    # Find maximum line length
    max_length = max(len(line) for line in bio_lines)

    print("\n╔" + "═" * (max_length + 2) + "╗")
    print("║" + " STUDENT BIO CARD ".center(max_length + 2) + "║")
    print("╠" + "═" * (max_length + 2) + "╣")

    for line in bio_lines:
        print("║ " + line.ljust(max_length) + " ║")

    print("╚" + "═" * (max_length + 2) + "╝")


if __name__ == "__main__":
    create_bio_card()