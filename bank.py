from datetime import date
from account import Account, Admin


class Bank:
    def __init__(self, name):
        self.name = name
        self.__balance = 10000000
        self.bank_status = True
        self.__accounts = []
        self.admin_list = []
        self.loan = 0
        self.loan_status = True

    def create_account(self, name, email, address, ac_type):
        account = Account(name, email, address, ac_type)
        if(account):
            self.__accounts.append(account)
        else:
            print('Please provide everything correctly')
        return account
    
    def add_admin(self, name, email):
        admin = Admin(name, email)
        self.admin_list.append(admin)
    
    def find_account(self, ac_number):
        for account in self.__accounts:
            if(account.account_number == ac_number):
                return account
        return None
    
    def delete_account(self, ac_number):
        account = self.find_account(ac_number)
        if(account):
            self.__accounts.remove(account)
            print(f'{account.account_holder} deleted succesfully!')
        else:
            print(f'Account does not exist')

    def show_all_account(self):
        for acc in self.__accounts:
            print(f'{acc.account_holder} \t {acc.account_number} \t {acc.account_type}')
    
    def add_balance(self, amount):
        self.__balance += amount
        print(f'{amount} added successfully!')
    
    def withdraw_balance(self, amount):
        self.__balance -= amount
        print(f'{amount} withdraw successfully!')
    
    def get_loan(self, account, amount):
        if(amount > 0 and amount < self.__balance and self.loan_status and account.loan_limit <= 2):
            self.__balance -= amount
            account.balance += amount
            self.loan += amount
            print(f'loan {amount} is given to {account.account_holder} successfully')
        else:
            print(f'loan is not available now try again next time')
    
    def check_loan(self):
        print(f'total loan : {self.loan}')
    
    def check_available_balance(self):
        if(self.__balance == True):
            return True
        else:
            return False

    def on_off_loan(self, value):
        if(value == True):
            self.loan_status = False
        elif(value == False):
            self.loan_status = True

    def find_admin(self, n, e):
        for i in self.admin_list:
            if(i.name == n and e == i.email):
                return i
        return None
    