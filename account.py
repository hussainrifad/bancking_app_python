from datetime import date

class Account:
    total_account = 0
    def __init__(self, name, email, address, ac_type):
        self.balance = 0
        self.account_number = (name.lower()+email.lower()).replace('.','')+str(Account.total_account+1)
        Account.total_account += 1
        self.account_holder = name
        self.account_type = ac_type
        self.account_holder_address = address
        self.loan_limit = 2
        self.transaction_history = []

    def __str__(self):
        return f'save {self.account_number} for further use'

    def add_money(self, bank, amount):
        if(amount > 0):
            bank.add_balance(amount)
            self.balance += amount
        else:
            print(f'Enter right amount of money')
    
    def withdraw_money(self, bank, amount):
        if(amount > 0 and amount < self.balance and amount < bank.check_available_balance()):
            self.balance -= amount
            bank.withdraw_balance(amount)
        else:
            if(amount > bank.check_available_balance()):
                print(f'bank is bankrupt now')
            else:
                print(f'withdrawal amount exceeded')
    
    def get_loan(self, bank, account, amount):
        bank.get_loan(account, amount)

    def check_balance(self):
        print(f'total balance : {self.balance}')
    
    def transfer_money(self, bank, account1, account_number, amount):
        account2 = bank.find_account(account_number)
        if(amount < account1.balance and bank.bank_status and account2):
            transaction = Transaction(account1, account2, amount)
            account1.balance -= amount
            account2.balance += amount
            self.transaction_history.append(transaction)
        else:
            if(bank.find_account(account2) == None):
                print('account not exsist')
            elif(bank.bank_status == False):
                print('bank is bankcrupt')
            else:
                print('please enter right amount of money')

    def check_transfer_history(self):
        for i in self.transaction_history:
            print(f'{i.send_by} send {i.amount} to {i.recieved_by} in {i.time}')


class Transaction:
    def __init__(self, account1, account2, amount):
        self.send_by = account1.account_holder
        self.send_by_number = account1.account_number
        self.recieved_by = account2.account_holder
        self.recieved_by_number = account2.account_number
        self.amount = amount
        self.time = date.today()
    
class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def delete_user_account(self, bank, ac_number):
        bank.delete_account(ac_number)
    
    def see_all_account(self, bank):
        bank.show_all_account()
    
    def check_balance(self, bank):
        print(bank.check_available_balance())
    
    def view_loan_amount(self, bank):
        bank.check_loan()
    
    def view_loan_status(self, bank):
        bank.loan_status()

    def change_loan_status(self, bank):
        bank.on_off_loan()

    def create_admin(bank, name, email):
        bank.add_admin(name, email)