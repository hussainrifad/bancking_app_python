# class Account:
#     total = 0
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.number = (name.lower()+email.lower()).replace('.','')+str(Account.total)
#         Account.total += 1

# ac1 = Account('Rifad', 'rifad@gmail.com')
# ac2 = Account('Nishad', 'nishad@gmail.com')

# print(ac1.number)
# print(ac2.number)

class Name:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} is added'

print(Name('rifad', 'dk'))