from bank import Bank
from account import Account, Admin

bank = Bank('AZBank')
admin = Admin('admin', 'admin@gmail.com')
account = None
run = True

while run:
    print('1. create user account')
    print('2. switch to admin')
    print('3. log in admin')
    print('4. exit')

    option = int(input('-> '))
    if(option == 1):
        name = input('enter name : ')
        email = input('enter email : ')
        address = input('enter address : ')
        acc_type = int(input('1. current account\n2. savings accoun\n-> '))
        if(acc_type == 1):
            acc_type = 'ca'
        else:
            acc_type = 'sa'
        account = bank.create_account(name, email, address, acc_type)
        print(f'account number : {account.account_number} save for future use')
        run2 = True
        while run2:
            print('1. deposit money')
            print('2. withdraw money')
            print('3. check balance')
            print('4. check transaction history')
            print('5. take loan')
            print('6. transfer money')
            print('7. exit')

            option1 = int(input('-> '))
            if(option1 == 1):
                amount = int(input('enter amount : '))
                account.add_money(bank, amount)
            elif(option1 == 2):
                amount = int(input('enter amount : '))
                account.withdraw_money(bank, amount)
            elif(option1 == 3):
                account.check_balance()
            elif(option1 == 4):
                account.check_transfer_history()
            elif(option1 == 5):
                amount = int(input('enter amount : '))
                account.get_loan(bank, account, amount)
            elif(option1 == 6):
                amount = int(input('enter amount : '))
                account_number = input('enter account number whrer to send money: ')
                account.transfer_money(bank, account, account_number, amount)
            elif(option1 == 7):
                run2 = False
    elif(option == 2):
        run2 = True
        while run2:
            print('1. create admin account')
            print('2. delete user account')
            print('3. see all user account')
            print('4. total balance')
            print('5. total loan amount')
            if(bank.loan_status == True):
                print('6. turn off loan option')
            else:
                print('6. turn on loan option')
            print('7. exit')

            option1 = int(input('-> '))
            if(option1 == 1):
                name = input('enter name : ')
                email = input('enter email : ')
                admin.create_admin(name, email)
            elif(option1 == 2):
                account_number = input('enter account number : ')
                admin.delete_user_account(bank, account_number)
            elif(option1 == 3):
                admin.see_all_account(bank)
            elif(option1 == 4):
                admin.check_balance(bank)
            elif(option1 == 5):
                admin.view_loan_amount(bank)
            elif(option1 == 6):
                admin.change_loan_status(bank)
            elif(option1 == 7):
                run2 = False
    elif(option == 3):
        name = input('enter admin name')
        email = input('enter email address')
        newAdmin = bank.find_admin(email, name)
        if(newAdmin):
            admin = newAdmin
            print(f'{admin.name} logged in successfully')
        else:
            print('please enter name and email correcty')
    elif(option == 4):
        run = False


# rifadrifad@gmailcom1