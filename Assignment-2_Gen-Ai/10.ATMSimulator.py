"""
Question 10: Simple ATM Simulator
Description: Simulates basic ATM operations.
"""

def atm_simulator():
    print("===== ATM SIMULATOR =====")

    balance = 10000  # Initial balance

    while True:
        try:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            # Check Balance
            if choice == 1:
                print(f"Current balance: ₹{balance:.2f}")

            # Deposit
            elif choice == 2:
                deposit_amount = float(input("Enter amount to deposit: "))

                if deposit_amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    balance += deposit_amount
                    print("Deposit successful!")
                    print(f"Updated balance: ₹{balance:.2f}")

            # Withdraw
            elif choice == 3:
                withdraw_amount = float(input("Enter amount to withdraw: "))

                if withdraw_amount <= 0:
                    print(" Withdrawal amount must be positive.")
                elif withdraw_amount > balance:
                    print(" Insufficient balance!")
                elif balance - withdraw_amount < 500:
                    print(" Minimum balance of ₹500 must be maintained.")
                else:
                    balance -= withdraw_amount
                    print("Withdrawal successful!")
                    print(f"New balance: ₹{balance:.2f}")

            # Exit
            elif choice == 4:
                print("Thank you for using ATM. Goodbye!")
                break

            else:
                print(" Invalid choice! Please select 1-4.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")


# Main execution
if __name__ == "__main__":
    atm_simulator()