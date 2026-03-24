"""
Question 9: Ticket Pricing System
Description: Calculates movie ticket price based on age and day discount.
"""

def ticket_pricing_system():
    print("===== MOVIE TICKET PRICING SYSTEM =====\n")

    try:
        # Taking inputs
        age = int(input("Enter age: "))
        day = input("Enter day of week: ").strip().lower()
        number_of_tickets = int(input("Enter number of tickets: "))

        if age < 0:
            raise ValueError("Age cannot be negative.")
        if number_of_tickets <= 0:
            raise ValueError("Number of tickets must be greater than 0.")

        # Age-based pricing
        if age < 3:
            base_price = 0
            category = "Free"
        elif 3 <= age <= 12:
            base_price = 150
            category = "Child"
        elif 13 <= age <= 59:
            base_price = 300
            category = "Adult"
        else:
            base_price = 200
            category = "Senior"

        # Day-based discount
        weekend_days = ["friday", "saturday", "sunday"]

        if day in weekend_days:
            discount_percentage = 20
        elif day in ["monday", "tuesday", "wednesday", "thursday"]:
            discount_percentage = 0
        else:
            raise ValueError("Invalid day entered.")

        # Calculations
        total_base_price = base_price * number_of_tickets
        discount_amount = total_base_price * (discount_percentage / 100)
        price_after_discount = total_base_price - discount_amount

        # Display Results
        print("\n===== BILL DETAILS =====")
        print(f"Category: {category}")
        print(f"Base price per ticket: ₹{base_price:.2f}")
        print(f"Number of tickets: {number_of_tickets}")
        print(f"Total base price: ₹{total_base_price:.2f}")
        print(f"Discount: {discount_percentage}%")
        print(f"Discount amount: ₹{discount_amount:.2f}")
        print(f"Final amount to pay: ₹{price_after_discount:.2f}")

    except ValueError as error:
        print("\n Error:", error)
    except Exception:
        print("\n Invalid input! Please try again.")


# Main execution
if __name__ == "__main__":
    ticket_pricing_system()