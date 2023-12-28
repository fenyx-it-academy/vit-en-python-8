class Account:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Transaction completed successfully. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Transaction completed successfully. New balance: {self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Total balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Account successfully created!")

    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print("Account successfully removed.")
                return
        print("Account not found.")

    def check_total_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        print(f"Total balance: {total_balance}")


bank = Bank()

while True:
    print("\nWelcome to the banking system! Please select an option:")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Remove account")
    print("5. Check total balance")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        acc_number = input("Enter account number: ")
        acc_name = input("Enter account holder name: ")
        starting_balance = float(input("Enter starting balance: "))
        new_account = Account(acc_number, acc_name, starting_balance)
        bank.add_account(new_account)

    elif choice == "2":
        acc_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        for acc in bank.accounts:
            if acc.account_number == acc_number:
                acc.deposit(amount)
                break
        else:
            print("Account not found.")

    elif choice == "3":
        acc_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        for acc in bank.accounts:
            if acc.account_number == acc_number:
                acc.withdraw(amount)
                break
        else:
            print("Account not found.")

    elif choice == "4":
        acc_number = input("Enter account number: ")
        bank.remove_account(acc_number)

    elif choice == "5":
        bank.check_total_balance()

    elif choice == "6":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")



