"""
Question 4: Age Calculator
Description: Calculates age in different units.
"""

from datetime import datetime

def age_calculator():
    print("===== AGE CALCULATOR =====\n")

    try:
        # Ask user whether they want exact calculation
        choice = input("Do you want exact age calculation? (yes/no): ").strip().lower()

        current_date = datetime.now()

        if choice == "yes":
            # BONUS: Exact birthdate calculation
            birth_day = int(input("Enter birth day (1-31): "))
            birth_month = int(input("Enter birth month (1-12): "))
            birth_year = int(input("Enter birth year (e.g., 2004): "))

            birth_date = datetime(birth_year, birth_month, birth_day)

            if birth_date > current_date:
                raise ValueError("Birth date cannot be in the future.")

            age_in_days = (current_date - birth_date).days
            current_age = age_in_days // 365

        else:
            # Basic calculation using only birth year
            birth_year = int(input("Enter your birth year: "))

            if birth_year > current_date.year:
                raise ValueError("Birth year cannot be in the future.")

            current_age = current_date.year - birth_year
            age_in_days = current_age * 365  # Approximate

        # Common calculations
        age_in_months = current_age * 12
        age_in_hours = age_in_days * 24
        age_in_minutes = age_in_hours * 60
        years_until_100 = 100 - current_age

        # Display results
        print("\nResults:")
        print(f"Current Age: {current_age} years")
        print(f"Age in months: {age_in_months}")
        print(f"Age in days (approx): {age_in_days}")
        print(f"Age in hours: {age_in_hours}")
        print(f"Age in minutes: {age_in_minutes}")
        print(f"Years until 100: {years_until_100}")

    except ValueError as error:
        print("\n Error:", error)
    except Exception:
        print("\n Invalid input! Please enter valid numbers.")


# Main execution
if __name__ == "__main__":
    age_calculator()