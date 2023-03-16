import random

class Account:
    def __init__(self, name, balance):
        self.bank = "SC은행"
        self.name = name
        self.balance = balance

        num1 = random.randint(100, 999)
        num2 = random.randint(10, 99)
        num3 = random.randint(100000, 999999)

        self.code = f"{num1}-{num2}-{num3}"

    def get_bank(self):
        return self.bank

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def get_code(self):
        return self.code

a = Account("tset","1")

# get informations of Account
def get_all_information(account):
    print(account.get_bank())
    print(account.get_name())
    print(account.get_balance())
    print(account.get_code())

get_all_information(a)   
