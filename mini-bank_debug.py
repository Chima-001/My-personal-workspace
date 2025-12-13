def main():
    balance = 100.00
    transactions = []

    while True:
        print("\nWelcome to the Mini Bank app. Enter a command:\nDeposit\nWithdraw\nBalance\nHistory\nQuit\n")
        cmd = input(">").strip()

        if cmd.lower() == "deposit".lower():
            try:
                amount = float(input("Amount: "))
                balance += amount
                transactions.append(("deposit", amount))
            except ValueError:
                print("Invalid input! Please input amount with digits only")

        elif cmd.lower() == "withdraw".lower():
            try:
                amount = float(input("Amount: "))
                if amount > balance:
                    print("Insufficient funds!")
                else:
                    balance -= amount
                transactions.append(("withdraw", amount))
            except ValueError:
                print("Invalid input! Please input amount with digits only")

        elif cmd.lower() == "balance".lower():
            print(f"Balance: {balance:.2f}")

        elif cmd.lower() == "history".lower():
            for t in transactions:
                print(f"{t[0]}: {t[1]:.2f}")

        elif cmd.lower() == "quit".lower():
            break
        
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()