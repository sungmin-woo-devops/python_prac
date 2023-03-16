import random

class Account:
    # 클래스 변수
    account_made = 0

    def __init__(self, name, balance):
        self.bank = "SC은행"
        self.name = name
        self.balance = balance

        num1 = random.randint(100, 999)
        num2 = random.randint(10, 99)
        num3 = random.randint(100000, 999999)

        self.code = f"{num1}-{num2}-{num3}"

        Account.account_made = Account.account_made + 1

    def get_bank(self):
        return self.bank

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def get_code(self):
        return self.code


# get informations of Account
def get_all_information(account):
    print(account.get_bank())
    print(account.get_name())
    print(account.get_balance())
    print(account.get_code())

print(Account.account_made)
kim = Account("김민수", 100)
lee = Account("이민수", 100)
print(Account.account_made)

