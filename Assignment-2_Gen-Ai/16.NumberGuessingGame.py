"""
Question 16: Number Guessing Game

Features:
- Computer selects a random number between 1 and 100
- User gets 7 attempts
- Shows whether guess is too high or too low
- Displays remaining attempts
- Congratulates on success
- Reveals number if user fails
- Option to play again
- Bonus:
    * Tracks best score (minimum attempts)
    * Provides hint when guess is within 5 of correct number
"""

import random  # Used to generate random number


def number_guessing_game():

    print("NUMBER GUESSING GAME")

    best_score = None  # Stores minimum attempts across games

    # Loop to allow multiple games
    while True:

        # Generate random number between 1 and 100
        secret_number = random.randint(1, 100)

        attempts_remaining = 7
        attempts_used = 0
        guessed_correctly = False

        print("\nA number has been selected between 1 and 100.")
        print("You have 7 attempts to guess it.")

        # Main guessing loop
        while attempts_remaining > 0:
            try:
                guess = int(input("\nEnter your guess: "))

                # Validate input range
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue

                attempts_used += 1
                attempts_remaining -= 1

                # Check guess
                if guess == secret_number:
                    print(f"Correct. You guessed the number in {attempts_used} attempts.")
                    guessed_correctly = True

                    # Update best score
                    if best_score is None or attempts_used < best_score:
                        best_score = attempts_used
                        print("This is your best score so far.")

                    break

                elif guess > secret_number:
                    print("Your guess is too high.")
                else:
                    print("Your guess is too low.")

                # Bonus hint if within 5
                if abs(guess - secret_number) <= 5:
                    print("Hint: You are very close.")

                print(f"Attempts remaining: {attempts_remaining}")

            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # If user fails
        if not guessed_correctly:
            print(f"\nGame Over. The correct number was {secret_number}.")

        # Display best score
        if best_score is not None:
            print(f"Best score (minimum attempts): {best_score}")

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if play_again != "yes":
            print("Thank you for playing.")
            break


# Run the program
if __name__ == "__main__":
    number_guessing_game()