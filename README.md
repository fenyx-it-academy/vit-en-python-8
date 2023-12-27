# vit-en-python-8

In this assignment, you will create a Python program that uses object-oriented programming to model a banking system. The program should allow a user to create and manage multiple bank accounts. Each account should have a balance and allow for deposit and withdrawal transactions.

Your program should include the following classes:

#### Account Class
`Attributes: account number, account holder name, balance`

`Methods: deposit, withdraw, check balance`

#### Bank Class
`Attributes: list of accounts`

`Methods: add account, remove account, check total balance`

Your program should have a menu-based interface that allows a user to create and manage multiple accounts. Here is an example of how the menu interface might work:

    Welcome to the banking system! Please select an option:

    1. Create account
    2. Deposit
    3. Withdraw
    4. Remove account
    5. Check total balance

    Create account:

    Enter account number: 12345
    Enter starting balance: 1000
    Account successfully created!


    Deposit:

    Enter account number: 12345
    Enter amount to deposit: 500
    Transaction completed successfully. New balance: 1500


    Withdraw:

    Enter account number: 12345
    Enter amount to withdraw: 200
    Transaction completed successfully.
    New balance: 1300


    Remove account:

    Enter account number: 12345
    Account successfully removed.


    Check total balance:

    Enter account number: 12345
    Total balance: 1300

    Exit:

    Exiting the program...
