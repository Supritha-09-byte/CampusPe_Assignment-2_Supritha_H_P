"""
Question 8: Leap Year Checker
Description: Checks whether a given year is a leap year
based on official leap year rules.
"""

def check_leap_year():
    print("===== LEAP YEAR CHECKER =====\n")

    try:
        year = int(input("Enter a year: "))

        if year <= 0:
            raise ValueError("Year must be a positive number.")

        # Leap year logic
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            is_leap = True
        else:
            is_leap = False

        # Display result with reason
        print("\n===== RESULT =====")
        print(f"Year: {year}")

        if is_leap:
            print("Status: Leap Year ")
            if year % 400 == 0:
                print("Reason: Divisible by 400.")
            elif year % 100 == 0:
                print("Reason: Divisible by 100 but also divisible by 400.")
            else:
                print("Reason: Divisible by 4 and not divisible by 100.")
        else:
            print("Status: NOT a Leap Year ")
            if year % 4 != 0:
                print("Reason: Not divisible by 4.")
            elif year % 100 == 0 and year % 400 != 0:
                print("Reason: Divisible by 100 but not divisible by 400.")
            else:
                print("Reason: Does not satisfy leap year conditions.")

    except ValueError as error:
        print("\n Error:", error)


# Main execution
if __name__ == "__main__":
    check_leap_year()