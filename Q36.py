class Bank:
    def _init_(self):
        self.accounts = {}

    def create_account(self, name, account_no, initial_balance):
        if account_no not in self.accounts:
            self.accounts[account_no] = {'name': name, 'balance': initial_balance}
            print(f"Account created successfully for {name} with account number {account_no}.")
        else:
            print(f"Account with account number {account_no} already exists.")

    def withdraw(self, account_no, amount):
        if account_no in self.accounts:
            if amount <= self.accounts[account_no]['balance']:
                self.accounts[account_no]['balance'] -= amount
                print(f"Withdrawal successful. Current balance: Rs{self.accounts[account_no]['balance']}")
            else:
                print("Insufficient funds. Withdrawal failed.")
        else:
            print(f"Account with account number {account_no} not found.")

    def deposit(self, account_no, amount):
        if account_no in self.accounts:
            self.accounts[account_no]['balance'] += amount
            print(f"Deposit successful. Current balance:Rs{self.accounts[account_no]['balance']}")
        else:
            print(f"Account with account number {account_no} not found.")

bank = Bank()

while True:
    print("\nBank Management Menu:")
    print("1. Create Account")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter your name: ")
        account_no = input("Enter account number: ")
        initial_balance = float(input("Enter initial balance: "))
        bank.create_account(name, account_no, initial_balance)
    elif choice == "2":
        account_no = input("Enter account number to withdraw from: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(account_no, amount)
    elif choice == "3":
        account_no = input("Enter account number to deposit to: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(account_no, amount)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")