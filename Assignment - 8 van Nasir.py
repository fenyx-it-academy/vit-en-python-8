class Account:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Transection completed succesfully. News balance: {
              self.balance}')

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'Transection completed succesfully. News balance: {
                self.balance}')
        else:
            print('Transection completed not succesfully')

    def Check_Balance(self):
        print('Totaal balance: {self.balance}')


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print('Account succesfully created:')

    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print('Account successfully removed.')
            return
        print("Account not found.")

    def check_totaal_balance(self):
        totaal_balance = sum(account.balance for account in self.accounts)
        print(f'Totaal balance: {totaal_balance}')


bank = Bank()

while True:
    print('Welcomr to banking system! Please select an option:')
    print('1. Create account\n2. Deposit\n3. Withdraw\n4. Remove account\n5. Check total balance\n5. Exit')

    choice = input('Enter your choice 1-6:')
    if choice == "1":
        Acc_No = input('Enter account Number:')
        Acc_name = input('Enter account holder name:')
        Starting_balance = float(input('Enter starting balance: '))
        New_account = Account(Acc_No, Acc_name, Starting_balance)
        bank.add_account(New_account)

    elif choice == "2":
        Acc_No = input('Enter account Number:')
        amount = float(input('Enter amount to deposit:'))
        for Acc in bank.accounts:
            if Acc.account_number == Acc_No:
                Acc.deposit(amount)
                break
        else:
            print('Account not found!')

    elif choice == "3":
        Acc_No = input('Enter account number:')
        amount = float(input('Enter amount to withdraw:'))
        for Acc in bank.accounts:
            if Acc.account_number == Acc_No:
                Acc.withdraw(amount)
                break
        else:
            print('account not found!')

    elif choice == "4":
        Acc_No = input('Enter account number:')
        bank.remove_account(Acc_No)

    elif choice == "5":
        Acc_No = input('Enter account number:')
        bank.check_totaal_balance()

    elif choice == "6":
        print("Exiting the program...")

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
