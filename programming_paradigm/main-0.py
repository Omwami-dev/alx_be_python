from bank_account import BankAccount
def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> [amount]")
        print("Operations: deposit, withdraw, display_balance")
        return

    # Initialize the BankAccount instance
    account = BankAccount()

    # Parse the operation and optional amount
    operation = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else None

    try:
        if operation == "deposit" and amount is not None:
            account.deposit(amount)
            print("Deposit successful.")
        elif operation == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        elif operation == "display_balance":
            print(account.display_balance())
        else:
            print("Invalid operation or missing amount.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()