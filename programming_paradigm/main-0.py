from bank_account import BankAccount
def main():
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command> [amount]")
        print("Commands: deposit, withdraw, display")
        return

    # Initialize the BankAccount instance
    account = BankAccount()

    # Parse the operation and optional amount
    command = sys.argv[1].lower()
    amount = float(sys.argv[2]) if len(sys.argv) > 2 else None

    try:
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command== "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        elif command == "display_balance":
            print(account.display_balance())
        else:
            print("Invalid command.")
    
if __name__ == "__main__":
    main()