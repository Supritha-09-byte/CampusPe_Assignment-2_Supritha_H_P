"""
Question 5: Bill Splitter
Description: Splits restaurant bill including tax and tip.
"""

def bill_splitter():
    print("===== RESTAURANT BILL SPLITTER =====\n")

    try:
        # Taking inputs
        total_bill = float(input("Enter total bill: "))
        number_of_people = int(input("Number of people: "))
        tax_percentage = float(input("Tax percentage: "))
        tip_percentage = float(input("Tip percentage: "))

        # Validations
        if total_bill < 0:
            raise ValueError("Bill amount cannot be negative.")
        if number_of_people <= 0:
            raise ValueError("Number of people must be greater than 0.")
        if tax_percentage < 0 or tip_percentage < 0:
            raise ValueError("Tax and Tip percentages cannot be negative.")

        # Calculations
        subtotal = total_bill
        tax_amount = subtotal * (tax_percentage / 100)
        bill_after_tax = subtotal + tax_amount
        tip_amount = bill_after_tax * (tip_percentage / 100)
        total_amount = bill_after_tax + tip_amount
        amount_per_person = total_amount / number_of_people

        # Display Results
        print("\n=== BILL BREAKDOWN ===")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax ({tax_percentage}%): ₹{tax_amount:.2f}")
        print(f"After tax: ₹{bill_after_tax:.2f}")
        print(f"Tip ({tip_percentage}%): ₹{tip_amount:.2f}")
        print(f"Total: ₹{total_amount:.2f}")
        print(f"Per person: ₹{amount_per_person:.2f}")

    except ValueError as error:
        print("\n Error:", error)
    except Exception:
        print("\n Invalid input! Please enter valid numbers.")


# Main execution
if __name__ == "__main__":
    bill_splitter()